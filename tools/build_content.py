"""Convert extracted woikr posts (tmp/raw/posts_all.json, pages_static.json) into Hugo content.

Outputs:
  site/content/posts/<section>-<slug>.md   one per post, url kept identical to the original
  site/content/about.md, site/content/advertise.md
  site/data/comments.json                 read-only comments keyed by post id
"""
import datetime as dt
import html as htmlmod
import json
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..")
RAW = os.path.join(ROOT, "tmp", "raw")
SITE = os.path.join(ROOT, "site")
MONTHS = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"], 1)}
MON_ABBR = {m[:3]: i for m, i in MONTHS.items()}


def load(name):
    d = json.load(open(os.path.join(RAW, name), encoding="utf-8"))
    return json.loads(d) if isinstance(d, str) else d


def clean_html(h):
    h = re.sub(r"https?://(?:www\.)?woikr\.com", "", h)
    h = h.replace('src="/wp/wp-content/', 'src="/wp-content/')
    h = h.replace('href="/wp/wp-content/', 'href="/wp-content/')
    h = re.sub(r"<(script|iframe|style)\b.*?</\1>", "", h, flags=re.S | re.I)
    h = re.sub(r"<!--.*?-->", "", h, flags=re.S)
    h = re.sub(r"\n{3,}", "\n\n", h)
    return h.strip()


EMAIL_LINK = re.compile(r'<a href="mailto:[^"]*">[^<]*</a>', re.I)
EMAIL_TEXT = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def redact_comment(h):
    """Commenters' personal email addresses are not published."""
    h = EMAIL_LINK.sub("[email removed]", h)
    return EMAIL_TEXT.sub("[email removed]", h)


def parse_info(info):
    """'Posted by Chirag in Android on Nov 8th, 2010 | Comments' -> (author, category, date)."""
    m = re.search(r"Posted by (.+?) in (.+?) on ([A-Za-z]{3})[a-z]* (\d{1,2})(?:st|nd|rd|th)?, (\d{4})", info)
    if not m:
        return None, None, None
    author, cat, mon, day, year = m.groups()
    d = dt.date(int(year), MON_ABBR[mon], int(day))
    return author.strip(), cat.strip(), d


def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def main():
    posts = load("posts_all.json")
    statics = load("pages_static.json")
    posts_dir = os.path.join(SITE, "content", "posts")
    os.makedirs(posts_dir, exist_ok=True)
    os.makedirs(os.path.join(SITE, "data"), exist_ok=True)
    comments_out = {}
    report = []
    for p in sorted(posts, key=lambda x: x["slug"]):
        slug = p["slug"].strip("/")
        section, _, leaf = slug.partition("/")
        pid = slug.replace("/", "-")
        author, cat, date = parse_info(p.get("info", ""))
        if not date:
            if p.get("date"):
                date = dt.datetime.fromisoformat(p["date"].replace("Z", "+00:00")).date()
            else:
                report.append(("no-date", slug))
                date = dt.date(2010, 1, 1)
        cats = [c for c in p.get("cats", []) if c]
        category = cat or (cats[0] if cats else section.title())
        tags = [c for c in cats if c.lower() != category.lower()]
        body = clean_html(p["html"])
        if not body:
            report.append(("empty-body", slug))
        fm = [
            "---",
            f"title: {yaml_str(htmlmod.unescape(p['title']))}",
            f"date: {date.isoformat()}",
            f"url: /{slug}/",
            f"author: {yaml_str(author or '')}",
            f"categories: [{yaml_str(category)}]",
            "tags: [" + ", ".join(yaml_str(t) for t in tags) + "]",
            f"comments_count: {len(p.get('comments', []))}",
            "---",
            "",
        ]
        with open(os.path.join(posts_dir, f"{pid}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(fm) + body + "\n")
        if p.get("comments"):
            comments_out[pid] = [
                {"author": c.get("author", ""), "date": c.get("date", ""),
                 "html": redact_comment(clean_html(c.get("html", "")))} for c in p["comments"]]
    # static pages
    for s in statics:
        if s.get("slug") == "feedback/" or "error" in s or not s.get("html", "").strip():
            report.append(("static-skipped", s.get("slug")))
            continue
        name = s["slug"].strip("/")
        body = clean_html(s["html"])
        fm = ["---", f"title: {yaml_str(s['title'])}", f"url: /{name}/", "type: page", "---", ""]
        with open(os.path.join(SITE, "content", f"{name}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(fm) + body + "\n")
    with open(os.path.join(SITE, "data", "comments.json"), "w", encoding="utf-8") as f:
        json.dump(comments_out, f, ensure_ascii=False, indent=1)
    print("posts written:", len(posts), "| with comments:", len(comments_out),
          "| comments total:", sum(len(v) for v in comments_out.values()))
    for r in report:
        print("NOTE", r)


if __name__ == "__main__":
    main()
