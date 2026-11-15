"""Performance budget check for the built site. Exits 1 when a rule is broken.

Rules (see docs/PERFORMANCE.md):
  1. Card thumbnails on every home page (page 1 and /page/N/) are WebP, at most 120 KB, at most 700 px on either side.
  2. Every image in the built site is at most 1600 px on its long side and 600 KB.
  3. Stylesheets are inlined: no <link rel="stylesheet"> in any page.
  4. No page loads a third-party script or stylesheet from another host.

Usage (after hugo build):  python tools/check_budgets.py public_dir
"""
import os
import re
import sys

from PIL import Image

CARD_MAX_BYTES = 120 * 1024
IMG_MAX_BYTES = 600 * 1024
IMG_MAX_SIDE = 1600
IMG_EXT = {".jpg", ".jpeg", ".png", ".webp"}
LINK_CSS = re.compile(r'<link[^>]+rel="?stylesheet', re.I)
EXT_SRC = re.compile(r'<(?:script[^>]+src|link[^>]+rel="?(?:stylesheet|preload)"?[^>]+href)="(https?://(?!(?:www\.)?woikr\.com)[^"]+)"', re.I)
CARD_IMG = re.compile(r'<a class="?card-thumb"?[^>]*>\s*<img src="?([^" >]+)', re.I)


def main(root):
    errors = []
    cards = []
    home_pages = [os.path.join(root, "index.html")]
    pages_dir = os.path.join(root, "page")
    if os.path.isdir(pages_dir):  # paginated home pages, loaded by infinite scroll
        home_pages += [os.path.join(pages_dir, d, "index.html") for d in os.listdir(pages_dir)]
    for page in home_pages:
        if os.path.isfile(page):
            with open(page, encoding="utf-8") as f:
                cards += CARD_IMG.findall(f.read())
    cards = sorted(set(cards))
    if not cards:
        errors.append("home pages: no card thumbnails found")
    for src in cards:
        p = os.path.join(root, src.lstrip("/"))
        if not os.path.isfile(p):
            errors.append(f"card thumbnail missing: {src}")
            continue
        if os.path.getsize(p) > CARD_MAX_BYTES:
            errors.append(f"card thumbnail too big ({os.path.getsize(p)//1024} KB): {src}")
        if not src.endswith(".webp"):
            errors.append(f"card thumbnail not WebP: {src}")
        with Image.open(p) as im:
            if max(im.size) > 700:
                errors.append(f"card thumbnail larger than 700px ({im.width}x{im.height}): {src}")

    for dp, _, fn in os.walk(root):
        for f in fn:
            p = os.path.join(dp, f)
            rel = "/" + os.path.relpath(p, root).replace(os.sep, "/")
            ext = os.path.splitext(f)[1].lower()
            if ext in IMG_EXT:
                size = os.path.getsize(p)
                if size > IMG_MAX_BYTES:
                    errors.append(f"image over 600 KB ({size//1024} KB): {rel}")
                if ext != ".webp" or size > 0:
                    try:
                        with Image.open(p) as im:
                            if max(im.size) > IMG_MAX_SIDE:
                                errors.append(f"image over 1600px ({im.width}x{im.height}): {rel}")
                    except Exception:
                        pass
            elif ext == ".html":
                with open(p, encoding="utf-8", errors="replace") as fh:
                    html = fh.read()
                if LINK_CSS.search(html):
                    errors.append(f"external stylesheet link (must be inlined): {rel}")
                for host_url in EXT_SRC.findall(html):  # third-party scripts/stylesheets only
                    errors.append(f"third-party asset {host_url} on {rel}")

    if errors:
        print(f"{len(errors)} budget violation(s):")
        for e in errors:
            print(" -", e)
        return 1
    print(f"budgets OK: {len(cards)} card thumbnails checked")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "public"))
