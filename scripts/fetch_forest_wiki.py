"""One-off snapshot of The Forest wiki into corpus/forest/ (RAG_V1_SPEC.md, Step 2).

Never called by the app.

    python scripts/fetch_forest_wiki.py                                            # full run, resumable
    python scripts/fetch_forest_wiki.py --pages "Skinny Mutant" Katana Characters  # sample run
"""
import argparse
import hashlib
import json
import os
import re
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

API_URL = "https://theforest.fandom.com/api.php"
SITE_URL = "https://theforest.fandom.com"
USER_AGENT = "norag-rag-course-project/1.0 (EPITA student project)"
OUT_DIR = Path(__file__).resolve().parent.parent / "corpus" / "forest"
MANIFEST_FILE = OUT_DIR / "MANIFEST.json"

MIN_SECONDS_BETWEEN_REQUESTS = 1.0
BACKOFF_SECONDS = [2, 4, 8]

# [DECISION D2] All non-redirect main-namespace pages, except the translated
# subpages that the English wiki also lists in the main namespace (e.g. "Katana/fr")
LANGUAGE_SUBPAGE = re.compile(r"/(ko|es|it|fr|pl)$")

# [DECISION D3] Elements removed before conversion: the spec's selectors, plus the
# equivalents this wiki actually uses (navboxes are wikitables with "margin: auto",
# inline images sit in div.thumb)
NAVBOX_SELECTOR = 'table.wikitable[style*="margin: auto"]'
REMOVE_SELECTORS = [
    ".navbox", ".mw-editsection", ".toc", "#toc", "figure", ".wikia-gallery", ".gallery",
    "img", "script", "style", "sup.reference", ".mw-references-wrap",
    NAVBOX_SELECTOR, ".thumb",
]

session = requests.Session()
session.headers["User-Agent"] = USER_AGENT
last_request_at = 0.0

# Reported at the end of the run, so nothing is dropped silently
removed_navboxes = Counter()
warnings = []


def api_get(params):
    """GET the API at most once per second. On HTTP 429/5xx back off 2, 4, 8 s, then fail."""
    global last_request_at
    for backoff in BACKOFF_SECONDS + [None]:
        wait = last_request_at + MIN_SECONDS_BETWEEN_REQUESTS - time.monotonic()
        if wait > 0:
            time.sleep(wait)
        last_request_at = time.monotonic()
        response = session.get(API_URL, params={**params, "format": "json"}, timeout=30)
        if response.status_code == 429 or response.status_code >= 500:
            if backoff is None:
                response.raise_for_status()
            print(f"  HTTP {response.status_code}, retrying in {backoff} s")
            time.sleep(backoff)
            continue
        response.raise_for_status()
        data = response.json()
        if "error" in data:
            raise RuntimeError(f"API error for {params}: {data['error']}")
        return data


def list_pages():
    params = {"action": "query", "list": "allpages", "apnamespace": 0,
              "apfilterredir": "nonredirects", "aplimit": "max"}
    pages = []
    while True:
        data = api_get(params)
        pages.extend(data["query"]["allpages"])
        if "continue" not in data:
            return pages
        params = {**params, **data["continue"]}


def latest_revids(pageids):
    """Current revid of each page (50 per request), used to skip pages already snapshotted."""
    revids = {}
    for i in range(0, len(pageids), 50):
        batch = pageids[i:i + 50]
        data = api_get({"action": "query", "prop": "info", "pageids": "|".join(map(str, batch))})
        for page in data["query"]["pages"].values():
            revids[page["pageid"]] = page["lastrevid"]
    return revids


def safe_name(title):
    return re.sub(r"[^A-Za-z0-9._()-]", "_", title.replace(" ", "_"))


def assign_file_names(pages):
    """File name per pageid. Case-insensitive collisions get a __<pageid> suffix."""
    names, taken = {}, set()
    for page in pages:
        name = safe_name(page["title"])
        if name.lower() in taken:
            name = f"{name}__{page['pageid']}"
        taken.add(name.lower())
        names[page["pageid"]] = name + ".md"
    return names


def page_url(title):
    path = quote(title.replace(" ", "_"), safe="/:()!,'")
    return f"{SITE_URL}/wiki/{path}"


def cell_text(cell):
    """Visible text of a table cell, with <br> line breaks kept as '; '."""
    for br in cell.find_all("br"):
        br.replace_with("\x1f")
    parts = (" ".join(part.split()) for part in cell.get_text().split("\x1f"))
    return "; ".join(part for part in parts if part)


def infobox_to_markdown(table, title):
    lines = []
    body = table.find("tbody", recursive=False) or table
    for row in body.find_all("tr", recursive=False):
        headers = row.find_all("th", recursive=False)
        cells = row.find_all("td", recursive=False)
        if len(cells) == 2 and not headers:
            lines.append(f"- **{cell_text(cells[0])}:** {cell_text(cells[1])}")
        elif len(headers) == 1 and not cells:
            header = headers[0]
            text = cell_text(header)
            classes = header.get("class", [])
            if "infoboxname" in classes:
                lines.append(f"**Infobox: {text}**")
            elif "infoboxdetails" in classes:
                lines.append(f"**{text}**")
            elif text and "infoboxcaption" not in classes and not header.find("i"):
                lines.append(text)
                warnings.append(f"{title}: unrecognised infobox header kept as text: {text[:80]}")
            # Otherwise an image row (empty once images are removed) or a caption: dropped
        else:
            text = cell_text(row)
            if text:
                lines.append(text)
                warnings.append(f"{title}: unrecognised infobox row kept as text: {text[:80]}")
    return "\n".join(lines)


def convert_page(title, html):
    soup = BeautifulSoup(html, "html.parser")
    for selector in REMOVE_SELECTORS:
        for element in soup.select(selector):
            if element.decomposed:
                continue
            if selector == NAVBOX_SELECTOR:
                removed_navboxes[" ".join(element.get_text(" ").split())[:30]] += 1
            element.decompose()

    # Swap each infobox for a placeholder, convert, then put the Markdown block back,
    # so markdownify doesn't escape the ** and - of the block
    infoboxes = []
    for table in soup.select("table.infoboxtable"):
        infoboxes.append(infobox_to_markdown(table, title))
        placeholder = soup.new_tag("p")
        placeholder.string = f"INFOBOX{len(infoboxes) - 1}PLACEHOLDER"
        table.replace_with(placeholder)

    markdown = markdownify(str(soup), heading_style="ATX", strip=["a"])
    for i, block in enumerate(infoboxes):
        markdown = markdown.replace(f"INFOBOX{i}PLACEHOLDER", block)
    # Collapse 3+ blank lines into 2
    markdown = re.sub(r"\n(?:[ \t]*\n){3,}", "\n\n\n", markdown)
    return markdown.strip()


def write_atomic(path, text):
    """Write via a temp file, so an interrupted run never leaves a half-written file."""
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(text, encoding="utf-8", newline="\n")
    os.replace(tmp, path)


def read_header(path):
    """(categories, revid) from an existing snapshot file, or None if there is no file."""
    if not path.exists():
        return None
    lines = path.read_text(encoding="utf-8").split("\n", 4)
    categories = lines[2].removeprefix("Categories: ")
    revid = int(lines[3].removeprefix("Revision: "))
    return (categories.split(", ") if categories else []), revid


def manifest_entry(page, file_name, revid, categories, path):
    data = path.read_bytes()
    return {"doc_id": f"forest/{file_name}", "title": page["title"], "pageid": page["pageid"],
            "revid": revid, "url": page_url(page["title"]), "categories": categories,
            "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


def main():
    parser = argparse.ArgumentParser(description="Snapshot The Forest wiki into corpus/forest/.")
    parser.add_argument("--pages", nargs="+", metavar="TITLE",
                        help="convert only these titles (sample run, MANIFEST.json is not written)")
    args = parser.parse_args()

    # Sanity check: stop if the API is unreachable or blocked
    try:
        stats = api_get({"action": "query", "meta": "siteinfo", "siprop": "statistics"})
    except (requests.RequestException, RuntimeError) as error:
        sys.exit(f"STOP: The Forest wiki API is unreachable or blocked ({error}).\n"
                 "Do not scrape the HTML pages or use mirrors.")
    print(f"Wiki reports {stats['query']['statistics']['articles']} articles.")

    pages = list_pages()
    excluded = [page["title"] for page in pages if LANGUAGE_SUBPAGE.search(page["title"])]
    pages = [page for page in pages if not LANGUAGE_SUBPAGE.search(page["title"])]
    print(f"{len(pages) + len(excluded)} non-redirect pages listed, "
          f"{len(excluded)} translated subpages excluded:")
    for title in excluded:
        print(f"  - {title}")
    # Names come from the full list, so a sample run gives the same names as the full run
    file_names = assign_file_names(pages)

    if args.pages:
        by_title = {page["title"]: page for page in pages}
        missing = [title for title in args.pages if title not in by_title]
        if missing:
            sys.exit(f"Not found among the non-redirect pages: {missing}")
        pages = [by_title[title] for title in args.pages]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    revids = latest_revids([page["pageid"] for page in pages])
    entries = []
    fetched = skipped = 0
    for n, page in enumerate(pages, 1):
        file_name = file_names[page["pageid"]]
        path = OUT_DIR / file_name
        header = read_header(path)
        if not args.pages and header and header[1] == revids[page["pageid"]]:
            categories, revid = header
            skipped += 1
        else:
            parsed = api_get({"action": "parse", "pageid": page["pageid"],
                              "prop": "text|categories|revid", "disableeditsection": 1,
                              "disabletoc": 1, "formatversion": 2})["parse"]
            categories = [c["category"].replace("_", " ")
                          for c in parsed["categories"] if not c.get("hidden")]
            # The Categories line is comma-separated, so a comma in a name would corrupt it
            if any("," in category for category in categories):
                raise ValueError(f"{page['title']}: category name contains a comma: {categories}")
            revid = parsed["revid"]
            content = (f"# {page['title']}\n"
                       f"Source: {page_url(page['title'])}\n"
                       f"Categories: {', '.join(categories)}\n"
                       f"Revision: {revid}\n\n"
                       f"{convert_page(page['title'], parsed['text'])}\n")
            write_atomic(path, content)
            fetched += 1
        entries.append(manifest_entry(page, file_name, revid, categories, path))
        if n % 50 == 0 or n == len(pages):
            print(f"[{n}/{len(pages)}] fetched {fetched}, skipped (same revid) {skipped}")

    print("Navboxes removed (first words, count):")
    for heading, count in removed_navboxes.most_common():
        print(f"  {count:4}  {heading}")
    if warnings:
        print(f"WARNING: {len(warnings)} infobox rows didn't match the mapping:")
        for warning in warnings:
            print(f"  - {warning}")

    if args.pages:
        print("Sample run: MANIFEST.json not written. Files:")
        for entry in entries:
            print(f"  corpus/{entry['doc_id']}")
        return

    manifest = {"source": SITE_URL,
                "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "article_count": len(entries),
                "files": entries}
    write_atomic(MANIFEST_FILE, json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {MANIFEST_FILE} with {len(entries)} articles.")

    listed = {entry["doc_id"].removeprefix("forest/") for entry in entries}
    stale = sorted(p.name for p in OUT_DIR.glob("*.md") if p.name not in listed)
    if stale:
        print(f"WARNING: {len(stale)} files in corpus/forest/ are not in the manifest "
              f"(page deleted or renamed on the wiki?):")
        for name in stale:
            print(f"  - {name}")


if __name__ == "__main__":
    main()