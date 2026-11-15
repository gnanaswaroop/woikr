"""Create card thumbnails for every post's `image:` front-matter value.

Cards display at most ~350 CSS px wide (700 px on 2x screens), so each card
gets a WebP whose longest side is 700 px, instead of the full-size upload.

  site/static/wp/wp-content/uploads/a/b.png
  -> site/static/thumbs/wp/wp-content/uploads/a/b.png.webp

Idempotent: existing thumbnails newer than their source are kept.
Run from the repo root:  python tools/make_thumbs.py
"""
import glob
import os
import re
import sys

from PIL import Image, ImageOps

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SITE = os.path.join(ROOT, "site")
STATIC = os.path.join(SITE, "static")
THUMBS = os.path.join(STATIC, "thumbs")
MAX_SIDE = 700  # cards show at most ~350 CSS px, so 700 covers 2x screens
QUALITY = 80
IMAGE_RE = re.compile(r'^image: "(.+)"$', re.M)


def card_images():
    found = set()
    for md in glob.glob(os.path.join(SITE, "content", "posts", "*.md")):
        with open(md, encoding="utf-8") as f:
            found.update(IMAGE_RE.findall(f.read()))
    return sorted(found)


def make(rel):
    src = os.path.join(STATIC, rel.lstrip("/"))
    # thumbs/<path under static, without leading slash>.webp
    dst = os.path.join(STATIC, "thumbs", rel.lstrip("/") + ".webp")
    if not os.path.isfile(src):
        return "missing-source"
    if os.path.isfile(dst) and os.path.getmtime(dst) >= os.path.getmtime(src):
        return "kept"
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im)
        if im.mode not in ("RGB", "RGBA"):
            im = im.convert("RGBA" if "A" in im.getbands() else "RGB")
        if max(im.size) > MAX_SIDE:
            scale = MAX_SIDE / max(im.size)
            im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
        im.save(dst, "WEBP", quality=QUALITY, method=6)
    return "made"


def main():
    counts = {}
    for rel in card_images():
        try:
            status = make(rel)
        except Exception as e:  # keep going; the budget check reports anything left behind
            status = "error"
            print("error", rel, e, file=sys.stderr)
        counts[status] = counts.get(status, 0) + 1
    print("card thumbnails:", counts)


if __name__ == "__main__":
    main()
