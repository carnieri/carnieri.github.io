#!/usr/bin/env python3
"""Generate an HTML image gallery for a folder of JPG images."""

import argparse
import html
import os
import sys
from pathlib import Path


def generate_gallery(folder: str, output: str | None = None) -> None:
    folder_path = Path(folder).resolve()
    if not folder_path.is_dir():
        print(f"Error: '{folder}' is not a valid directory.", file=sys.stderr)
        sys.exit(1)

    images = sorted(
        p.name for p in folder_path.iterdir() if p.suffix.lower() in (".jpg", ".jpeg")
    )

    if not images:
        print(f"No JPG images found in '{folder}'.", file=sys.stderr)
        sys.exit(1)

    output_path = Path(output) if output else folder_path / "gallery.html"
    folder_name = html.escape(folder_path.name)

    image_cards = "\n".join(
        f'      <div class="card">'
        f'<a href="{html.escape(img)}" target="_blank">'
        f'<img src="{html.escape(img)}" alt="{html.escape(img)}" loading="lazy">'
        f"</a><p>{html.escape(img)}</p></div>"
        for img in images
    )

    page = f"""\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gallery – {folder_name}</title>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: system-ui, sans-serif; background: #1a1a2e; color: #eee; padding: 2rem; }}
    h1 {{ text-align: center; margin-bottom: 1.5rem; font-size: 1.8rem; }}
    .gallery {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1rem; }}
    .card {{
      background: #16213e; border-radius: 8px; overflow: hidden;
      transition: transform 0.2s;
    }}
    .card:hover {{ transform: scale(1.03); }}
    .card img {{ width: 100%; height: 200px; object-fit: cover; display: block; }}
    .card p {{ padding: 0.5rem; text-align: center; font-size: 0.85rem; word-break: break-all; }}
    a {{ text-decoration: none; }}
  </style>
</head>
<body>
  <h1>Gallery – {folder_name}</h1>
  <div class="gallery">
{image_cards}
  </div>
</body>
</html>"""

    output_path.write_text(page, encoding="utf-8")
    print(f"Gallery created: {output_path}  ({len(images)} images)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate an HTML gallery of JPG images."
    )
    parser.add_argument("folder", help="Path to folder containing JPG images")
    parser.add_argument(
        "-o", "--output", help="Output HTML file path (default: <folder>/gallery.html)"
    )
    args = parser.parse_args()
    generate_gallery(args.folder, args.output)
