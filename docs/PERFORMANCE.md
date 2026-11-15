# Performance rules

These rules keep the site fast on phones as content is added. The deploy
workflow enforces the image and asset rules; a violation fails the deploy.

## What the workflow does on every deploy

1. `tools/make_thumbs.py` creates a WebP card thumbnail (longest side 700 px)
   for every post's `image:` front-matter value. Nothing to do by hand.
2. `tools/optimize_images.py` shrinks any image in `site/static` that is over
   150 KB or over 1600 px on its long side. Same path and format, so links keep
   working.
3. Hugo builds the site, minifies it, and inlines the stylesheet.
4. `tools/check_budgets.py` checks the built site and fails the deploy when a
   rule below is broken.

## Rules for content

- **Images in posts:** upload at up to 1600 px wide. Larger files are shrunk
  automatically on deploy, but avoid uploading very large originals.
- **Card thumbnails:** do not hand-pick sizes. Set the post's first image; the
  thumbnail is generated automatically.
- **Infographics and very tall images:** they are fine in the body, but the card
  thumbnail is capped at 700 px on its longest side.
- **No third-party scripts or stylesheets** on pages (ads, widgets, fonts, embeds
  that load from another host). Each one adds a network round trip before the
  page can render. Ask before adding one.
- **No external stylesheets:** `site/assets/css/style.css` is inlined into every
  page. Add styles there, not in new files.
- **Scripts:** keep them small and load them with `defer`.

## Budgets enforced by `tools/check_budgets.py`

| Rule | Limit |
| --- | --- |
| Card thumbnails (all home pages) | WebP, at most 120 KB, longest side 700 px |
| Any image in the built site | longest side 1600 px, at most 600 KB |
| Stylesheets | inlined; no `<link rel="stylesheet">` on any page |
| Third-party scripts and stylesheets | none |

## Known limit: browser caching

GitHub Pages sets short cache lifetimes (about 10 minutes) on every file, and the
site cannot change that. PageSpeed reports "Use efficient cache lifetimes" for
this reason. The fix would be to put Cloudflare (or a similar CDN) in front of
the domain, which is a DNS change and needs a decision.

## Running the checks locally

From the repo root:

    pip install -r tools/requirements.txt
    python tools/make_thumbs.py
    python tools/optimize_images.py --dry-run
    cd site && hugo --destination ../tmp/check-build && cd ..
    python tools/check_budgets.py tmp/check-build
