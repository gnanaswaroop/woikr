"""Download woikr.com media referenced by extracted posts from the Wayback Machine.

Reads tmp/raw/img_urls.json, writes files to tmp/images/<path after woikr.com/>.
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.join(os.path.dirname(__file__), "..", "tmp")
OUT = os.path.join(ROOT, "images")
TIMESTAMPS = ["20231225043137", "20211229101847", "20180601000000"]
HOST_RE = re.compile(r"^https?://(?:www\.)?woikr\.com/(.+)$", re.I)


def local_path(url):
    m = HOST_RE.match(url)
    if not m:
        return None
    rel = urllib.parse.unquote(m.group(1).split("?")[0].split("#")[0])
    if not rel.startswith("wp/wp-content/uploads/"):
        return None
    return rel[len("wp/"):]  # wp-content/uploads/...


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "woikr-migration/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read(), r.headers.get("Content-Type", "")


def download(url):
    rel = local_path(url)
    if not rel:
        return url, "skip", None
    dest = os.path.join(OUT, rel)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return url, "exists", rel
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    src = re.sub(r"^https?://(www\.)?", "http://", url)
    last = None
    for ts in TIMESTAMPS:
        try:
            data, ctype = fetch(f"https://web.archive.org/web/{ts}id_/{src}")
            if "text/html" in ctype.lower() and not rel.lower().endswith((".html", ".htm")):
                last = "html-response"
                continue
            if len(data) < 16:
                last = "tiny"
                continue
            with open(dest, "wb") as f:
                f.write(data)
            return url, f"ok@{ts}", rel
        except Exception as e:  # noqa: BLE001
            last = str(e)[:120]
    return url, f"fail:{last}", rel


def main():
    urls = json.load(open(os.path.join(ROOT, "raw", "img_urls.json"), encoding="utf-8"))
    results = []
    with ThreadPoolExecutor(max_workers=4) as ex:
        for res in ex.map(download, urls):
            results.append(res)
    json.dump(results, open(os.path.join(ROOT, "raw", "image_results.json"), "w", encoding="utf-8"), indent=1)
    import collections
    print(collections.Counter(r[1].split("@")[0].split(":")[0] for r in results))
    fails = [r for r in results if r[1].startswith("fail")]
    print("failed:", len(fails))
    for r in fails[:40]:
        print(" ", r[0], r[1])


if __name__ == "__main__":
    sys.exit(main())
