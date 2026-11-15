"""Check every internal link and image in the built site exists.

Usage: python tools/crawl_links.py <public-dir>
Reports broken targets grouped by the target path, with the pages that link to them.
"""
import collections
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

root = os.path.abspath(sys.argv[1])
BASE = "/"


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.found = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for k in ("href", "src"):
            if a.get(k):
                self.found.append(a[k])


def exists(path):
    rel = path.lstrip("/")
    cands = [os.path.join(root, rel)]
    if not rel or rel.endswith("/"):
        cands.append(os.path.join(root, rel, "index.html"))
    else:
        cands.append(os.path.join(root, rel, "index.html"))
    return any(os.path.isfile(c) for c in cands)


broken = collections.defaultdict(set)
checked = 0
for dp, _, fs in os.walk(root):
    for f in fs:
        if not f.endswith(".html"):
            continue
        page = os.path.join(dp, f)
        src = "/" + os.path.relpath(page, root).replace(os.sep, "/")
        src = re.sub(r"index\.html$", "", src)
        p = Links()
        p.feed(open(page, encoding="utf-8", errors="replace").read())
        for raw in p.found:
            if raw.startswith(("http:", "https:", "mailto:", "#", "javascript:", "data:", "tel:")):
                continue
            parts = urlsplit(raw)
            if parts.netloc and parts.netloc not in ("woikr.com", "www.woikr.com"):
                continue
            target = unquote(parts.path)
            if not target:
                continue
            if not target.startswith("/"):
                target = os.path.normpath(os.path.join(os.path.dirname(src), target)).replace(os.sep, "/")
            checked += 1
            if not exists(target):
                broken[target].add(src)

print("links checked:", checked, "| broken targets:", len(broken))
for t, srcs in sorted(broken.items(), key=lambda kv: -len(kv[1])):
    print(f"{len(srcs):5d}  {t}   e.g. from {sorted(srcs)[0]}")
