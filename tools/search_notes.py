#!/usr/bin/env python3
"""Search the vault. Ranks notes by title, tags, then body text.

Usage:
    python3 tools/search_notes.py dharma
    python3 tools/search_notes.py "key exchange" --limit 5
    python3 tools/search_notes.py --tag cryptography
    python3 tools/search_notes.py hash --type permanent
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_index as bi  # noqa: E402
import check_backlinks as cb  # noqa: E402

TAGS_RE = re.compile(r"(?m)^tags:\s*\[(.*?)\]\s*$")
TYPE_RE = re.compile(r"(?m)^type:\s*[\"']?([A-Za-z_-]+)")


def type_of(text: str) -> str:
    match = TYPE_RE.search(text)
    return match.group(1).casefold() if match else ""


def tags_of(text: str) -> list[str]:
    match = TAGS_RE.search(text)
    if not match:
        return []
    return [t.strip().strip("\"'").casefold() for t in match.group(1).split(",") if t.strip()]


def score(query_terms: list[str], names: list[str], tags: list[str], body: str) -> float:
    names_l = [n.casefold() for n in names]
    title_l, body_l = " ".join(names_l), body.casefold()
    total = 0.0
    if " ".join(query_terms) in names_l:
        total += 50  # exact title
    for term in query_terms:
        if term in title_l:
            total += 10
        if any(term in tag for tag in tags):
            total += 4
        hits = body_l.count(term)
        if hits:
            total += min(hits, 10)
    if query_terms and all(t in title_l or t in body_l for t in query_terms):
        total *= 1.5  # every term present
    return total


def main() -> None:
    parser = argparse.ArgumentParser(description="Search the literature-notes vault.")
    parser.add_argument("query", nargs="*", help="words to search for")
    parser.add_argument("--tag", help="only notes with this tag")
    parser.add_argument("--type", help="only notes of this type (permanent, literature, research, journal)")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()
    if not args.query and not args.tag:
        parser.error("give search words or --tag")

    terms = [t.casefold() for t in " ".join(args.query).split()]
    results = []
    for path in cb.collect_notes():
        text = cb.read_text(path)
        tags = tags_of(text)
        if args.tag and args.tag.casefold() not in tags:
            continue
        if args.type and type_of(text) != args.type.casefold():
            continue
        title = cb.note_title(path, text) or path.stem
        s = score(terms, [title, path.stem], tags, bi.body_of(text)) if terms else 1.0
        if s > 0:
            results.append((s, title, cb.rel(path), bi.hook(text)))

    results.sort(key=lambda r: (-r[0], r[1].casefold()))
    if not results:
        print("No matches.")
        return
    for s, title, rel_path, line in results[: args.limit]:
        print(f"{title}  ({rel_path})")
        if line:
            print(f"    {line}")


if __name__ == "__main__":
    main()
