"""Build the Hugo site content from the extracted woikr WordPress backup (tmp/backup/*.json).

Preserves rendered URLs:
  posts  -> /<lowest-id category slug>/<post_name>/   (WordPress %category%/%postname%)
  pages  -> /<post_name>/
  redirection rules -> Hugo aliases on the target post, so old paths keep working
  media  -> /wp/wp-content/uploads/... (paths exactly as the original HTML references them)
Comments: approved only; commenter email and IP are not written.
"""
import collections
import html as htmlmod
import json
import os
import re
from urllib.parse import urlsplit

ROOT = os.path.join(os.path.dirname(__file__), "..")
BK = os.path.join(ROOT, "tmp", "backup")
SITE = os.path.join(ROOT, "site")
RAW = os.path.join(ROOT, "tmp", "raw")
SITE_HOST = re.compile(r"https?://(?:www\.)?woikr\.com", re.I)
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
SHORTCODE_WRAP = re.compile(r"\[caption[^\]]*\](.*?)\[/caption\]", re.S | re.I)
SHORTCODE_TAG = re.compile(r"\[/?(?:sharebar|gallery|embed|audio|video|caption)[^\]]*\]", re.I)
ATTR_NOISE = re.compile(r'\s(?:style|border|align|allowtransparency|scrolling|frameborder)="[^"]*"', re.I)
SCRIPT = re.compile(r"<(script|iframe|style|ins)\b.*?</\1>", re.S | re.I)
COMMENT = re.compile(r"<!--.*?-->", re.S)
EMAIL_IN_TEXT = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
MEDIA_RE = re.compile(r'(?:src|href)="((?:https?://(?:www\.)?woikr\.com)?/?wp/wp-content/uploads/[^"]+)"')


def load(t):
    return json.load(open(os.path.join(BK, f"{t}.json"), encoding="utf-8"))


BLOCK_START = re.compile(r"^\s*</?(p|div|h[1-6]|ul|ol|li|blockquote|table|tr|td|th|pre|hr|img|iframe|figure|section|article|dl|dt|dd)\b", re.I)
BLOCK_END = re.compile(r"</(p|div|h[1-6]|ul|ol|li|blockquote|table|pre|figure)>\s*$", re.I)


def autop_lite(h):
    """WordPress wpautop-style: a single newline between inline text becomes a <br>."""
    h = h.replace("\r\n", "\n").replace("\r", "\n")
    lines = h.split("\n")
    out = []
    for i, line in enumerate(lines):
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        keep = (not line.strip() or BLOCK_END.search(line)
                or not nxt.strip() or BLOCK_START.match(nxt))
        out.append(line if keep else line + "<br>")
    return "\n".join(out)


def clean_body(h):
    h = autop_lite(h)
    h = SHORTCODE_WRAP.sub(lambda m: m.group(1), h)
    h = SHORTCODE_TAG.sub("", h)
    h = SCRIPT.sub("", h)
    h = COMMENT.sub("", h)
    h = ATTR_NOISE.sub("", h)
    h = SITE_HOST.sub("", h)  # root-relative; keeps /wp/wp-content/... paths
    # Individuals' and press contact addresses quoted in old articles are not republished.
    h = EMAIL_IN_TEXT.sub(lambda m: m.group(0) if m.group(0).endswith("bot.talk.google.com") else "[email removed]", h)
    return h.strip()


def yq(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def text(s):
    return htmlmod.unescape(s or "")


def main():
    posts_all = load("wp_posts")
    tt = {x["term_taxonomy_id"]: x for x in load("wp_term_taxonomy")}
    terms = {x["term_id"]: x for x in load("wp_terms")}
    rel = collections.defaultdict(list)
    for r in load("wp_term_relationships"):
        rel[r["object_id"]].append(r["term_taxonomy_id"])

    def term_list(pid, tax):
        return [tt[t] for t in rel[pid] if t in tt and tt[t]["taxonomy"] == tax]

    # clear previously generated content (feedback.md is hand-written and kept)
    for f in os.listdir(os.path.join(SITE, "content", "posts")):
        os.remove(os.path.join(SITE, "content", "posts", f))
    keep_pages = {"about", "archives", "contests", "reviews", "iphone", "advertise"}

    users = {u["ID"]: u for u in load("wp_users")}  # ID, user_nicename, display_name only
    published = [x for x in posts_all if x["post_type"] == "post" and x["post_status"] == "publish"]
    url_of = {}
    post_fm = {}
    for x in published:
        cats = sorted(term_list(x["ID"], "category"), key=lambda t: t["term_id"])  # WP uses lowest term_id
        cslug = terms[cats[0]["term_id"]]["slug"] if cats else "uncategorized"
        url = f"/{cslug}/{x['post_name']}/"
        url_of[url] = x["post_name"]
        post_fm[x["post_name"]] = {
            "x": x,
            "url": url,
            "cats": [terms[c["term_id"]]["name"] for c in cats] or ["Uncategorized"],
            "tags": [terms[t["term_id"]]["name"] for t in term_list(x["ID"], "post_tag")],
            "aliases": [],
            "author": users.get(x["post_author"], {}),
        }

    # redirection rules -> aliases on the target post
    red_ok = red_skip = 0
    for r in load("wp_redirection_items"):
        src = (r.get("url") or "").split("?")[0]
        target = urlsplit(r.get("action_data") or "").path
        if target in url_of and src and src != target and src not in url_of:
            aliases = post_fm[url_of[target]]["aliases"]
            if src not in aliases:
                aliases.append(src)
            red_ok += 1
        else:
            red_skip += 1

    # old category paths that visitors requested (from the 404 log) -> current post URL
    cat_slugs = {x["slug"] for x in load("wp_terms")}
    by_name = {v["x"]["post_name"]: v for v in post_fm.values()}
    seen_404 = collections.Counter(re.sub(r"[?#].*", "", r.get("url") or "") for r in load("wp_redirection_404"))
    recover = []
    recategorised = 0
    for path, hits in seen_404.items():
        parts = path.strip("/").split("/")
        if len(parts) != 2 or parts[0] not in cat_slugs or "&" in path or " " in path:
            continue
        slug = parts[1]
        if slug in by_name:
            fm = by_name[slug]
            if path != fm["url"] and path not in fm["aliases"]:
                fm["aliases"].append(path)
                recategorised += 1
        elif hits >= 5:
            recover.append({"path": path, "hits": hits})
    with open(os.path.join(RAW, "archive_recovery.json"), "w", encoding="utf-8") as f:
        json.dump(sorted(recover, key=lambda r: -r["hits"]), f, ensure_ascii=False)
    print("old category paths aliased", recategorised, "| posts to recover from archive", len(recover))

    # approved comments only, keyed by post_name
    id2name = {x["ID"]: x["post_name"] for x in published}
    grouped = collections.defaultdict(list)
    for c in load("wp_comments"):
        if c["comment_approved"] == "1" and c["comment_post_ID"] in id2name:
            grouped[id2name[c["comment_post_ID"]]].append(c)
    comment_data = {}
    for name, cs in grouped.items():
        cs.sort(key=lambda c: c["comment_date"])
        comment_data[name] = [{
            "author": text(c["comment_author"]),
            "date": c["comment_date"][:16],
            "html": EMAIL.sub("[email removed]", htmlmod.escape(text(c["comment_content"]))).replace("\n", "<br>"),
        } for c in cs]

    for name, fm in post_fm.items():
        x = fm["x"]
        lines = ["---", f"title: {yq(text(x['post_title']))}",
                 f"date: {x['post_date'].replace(' ', 'T')}",
                 f"url: {fm['url']}",
                 f"categories: [{', '.join(yq(text(c)) for c in fm['cats'])}]",
                 f"tags: [{', '.join(yq(text(t)) for t in fm['tags'])}]"]
        au = fm["author"]
        if au.get("user_nicename"):
            lines.append(f"author: {yq(text(au.get('display_name') or au['user_nicename']))}")
            lines.append(f"authors: [{yq(au['user_nicename'])}]")  # /author/<nicename>/ archive
        if fm["aliases"]:
            lines.append("aliases: [" + ", ".join(yq(a) for a in fm["aliases"]) + "]")
        lines += ["---", ""]
        with open(os.path.join(SITE, "content", "posts", f"{name}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + clean_body(x["post_content"]) + "\n")

    # pages with real URLs
    page_count = 0
    for x in posts_all:
        if x["post_type"] == "page" and x["post_status"] == "publish" and x["post_name"] in keep_pages:
            lines = ["---", f"title: {yq(text(x['post_title']))}", f"url: /{x['post_name']}/", "type: page"]
            if x["post_name"] == "advertise":
                lines.append("hidden: true")  # served at its URL, kept out of the menu
            lines += ["---", ""]
            with open(os.path.join(SITE, "content", f"{x['post_name']}.md"), "w", encoding="utf-8") as f:
                f.write("\n".join(lines) + clean_body(x["post_content"]) + "\n")
            page_count += 1

    with open(os.path.join(SITE, "data", "comments.json"), "w", encoding="utf-8") as f:
        json.dump(comment_data, f, ensure_ascii=False)

    # media referenced by content, plus attachment guids (downloader input)
    media = set()
    for x in posts_all:
        if x["post_type"] in ("post", "page") and x["post_status"] == "publish":
            for m in MEDIA_RE.finditer(x["post_content"]):
                media.add("/" + SITE_HOST.sub("", m.group(1)).lstrip("/"))
    for x in posts_all:
        if x["post_type"] == "attachment" and "/wp-content/uploads/" in (x.get("guid") or ""):
            media.add("/" + x["guid"].split("woikr.com/", 1)[-1].lstrip("/"))
    media = sorted(media)
    with open(os.path.join(RAW, "backup_media.json"), "w", encoding="utf-8") as f:
        json.dump(media, f)

    print("published posts", len(published), "| pages", page_count)
    print("comments (approved)", sum(len(v) for v in comment_data.values()), "on", len(comment_data), "posts")
    print("redirect rules applied", red_ok, "not applied", red_skip)
    print("media paths referenced", len(media))


if __name__ == "__main__":
    main()
