#!/usr/bin/env python3
"""Fail if the built site has broken internal links, missing alts, or weak page structure."""

from html.parser import HTMLParser
from pathlib import Path

SITE = Path(__file__).resolve().parents[1] / "site"


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
        self.srcs = []
        self.ids = set()
        self.images = []
        self.h1 = 0
        self.has_main = False
        self.has_title = False
        self.has_description = False
        self.skip = 0
        self._capture_title = False

    def handle_starttag(self, tag, attrs):
        attr = {key: value or "" for key, value in attrs}
        if tag in ("script", "style"):
            self.skip += 1
        if "id" in attr and attr["id"]:
            self.ids.add(attr["id"])
        if tag == "a" and "href" in attr:
            self.hrefs.append(attr["href"])
        if tag in ("img", "script", "iframe") and "src" in attr:
            self.srcs.append((tag, attr["src"]))
        if tag == "img":
            self.images.append(attr)
        if tag == "link" and attr.get("href") and not attr.get("href", "").startswith("http"):
            self.srcs.append(("link", attr["href"]))
        if tag == "h1":
            self.h1 += 1
        if tag == "main":
            self.has_main = True
        if tag == "title":
            self._capture_title = True
            self.has_title = True
        if tag == "meta" and attr.get("name") == "description" and attr.get("content"):
            self.has_description = True

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.skip:
            self.skip -= 1
        if tag == "title":
            self._capture_title = False


def local_target(url: str):
    if not url or url.startswith(("#", "mailto:", "tel:", "http://", "https://", "data:")):
        return None
    path, _, fragment = url.partition("#")
    return path or None, fragment


def main() -> None:
    errors = []
    html_files = sorted(SITE.glob("*.html"))
    if not html_files:
        raise SystemExit("No HTML files in site/. Run scripts/build_site.py first.")

    parsed = {}
    for file in html_files:
        parser = Parser()
        parser.feed(file.read_text(encoding="utf-8"))
        parsed[file.name] = parser
        if parser.h1 != 1:
            errors.append(f"{file.name}: expected 1 h1, found {parser.h1}")
        if not parser.has_main:
            errors.append(f"{file.name}: missing <main>")
        if not parser.has_title:
            errors.append(f"{file.name}: missing <title>")
        if not parser.has_description:
            errors.append(f"{file.name}: missing meta description")
        for image in parser.images:
            alt = image.get("alt")
            if alt is None:
                errors.append(f"{file.name}: img missing alt ({image.get('src')})")
            elif alt == "" and "logo-white" not in image.get("src", ""):
                errors.append(f"{file.name}: empty alt on {image.get('src')}")

    for name, parser in parsed.items():
        for href in parser.hrefs:
            target = local_target(href)
            if target is None:
                if href.startswith("#"):
                    fragment = href[1:]
                    if fragment and fragment not in parser.ids:
                        errors.append(f"{name}: missing id for {href}")
                continue
            path, fragment = target
            destination = (SITE / path).resolve()
            try:
                destination.relative_to(SITE.resolve())
            except ValueError:
                errors.append(f"{name}: link escapes site: {href}")
                continue
            if not destination.exists():
                errors.append(f"{name}: broken link {href}")
                continue
            if fragment and destination.suffix == ".html":
                if destination.name not in parsed:
                    other = Parser()
                    other.feed(destination.read_text(encoding="utf-8"))
                    parsed[destination.name] = other
                if fragment not in parsed[destination.name].ids:
                    errors.append(f"{name}: missing id {fragment} in {destination.name}")
        for _tag, src in parser.srcs:
            target = local_target(src)
            if target is None:
                continue
            path, _fragment = target
            destination = (SITE / path).resolve()
            if not destination.exists():
                errors.append(f"{name}: missing file {src}")

    if errors:
        print("\n".join(errors))
        raise SystemExit(f"{len(errors)} problem(s)")
    print(f"Checked {len(html_files)} pages. Internal links, assets, headings, and alts look sound.")


if __name__ == "__main__":
    main()
