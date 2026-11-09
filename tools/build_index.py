#!/usr/bin/env python3
"""Build INDEX.md: one line per note, grouped by area, with a short hook.

The hook is the first meaningful line of the note body, so a sutra-style
note shows its essence right in the index. Output is deterministic (no
dates, sorted), so the GitHub Action only commits when notes change.

Usage:
    python3 tools/build_index.py          # write INDEX.md
    python3 tools/build_index.py --check  # exit 1 if INDEX.md is stale
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_backlinks as cb  # noqa: E402

ROOT = cb.ROOT
INDEX = cb.INDEX
HOOK_LEN = 90

# (heading, path prefix) in display order. First match wins.
SECTIONS = [
    ("Computer science · Cryptography", "content/domains/computer-science/cryptography/"),
    ("Computer science · Security", "content/domains/computer-science/security/"),
    ("Computer science · Coding practices", "content/domains/computer-science/coding-practices/"),
    ("Computer science · Design patterns", "content/domains/computer-science/design-patterns/"),
    ("Computer science · Machine learning", "content/domains/computer-science/machine-learning/"),
    ("Computer science · Knowledge management", "content/domains/computer-science/knowledge-management/"),
    ("Sanskrit & Indian philosophy", "content/domains/humanities/sanskrit-literature/"),
    ("History", "content/domains/humanities/history/"),
    ("Mathematics", "content/domains/mathematics/"),
    ("Wellness", "content/domains/wellness/"),
    ("People", "content/people/"),
    ("Research (workbench)", "content/research/"),
    ("Books & highlights", "content/media/books/"),
    ("Articles", "content/media/articles/"),
    ("Podcasts & videos", "content/media/"),
    ("Music", "music/"),
    ("Finance", "finances/"),
    ("Legacy pages", "pages/"),
]

SKIP_NAMES: set[str] = set()
SKIP_PREFIXES: tuple[str, ...] = ()
JOURNAL_PREFIXES = ("content/journal/", "journals/")

LINK_RE = re.compile(r"!?\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
MD_LINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")


def body_of(text: str) -> str:
    match = cb.FRONTMATTER_RE.match(text)
    return text[match.end():] if match else text


def clean(line: str) -> str:
    line = LINK_RE.sub(lambda m: m.group(2) or m.group(1), line)
    line = MD_LINK_RE.sub(lambda m: m.group(1), line)
    line = re.sub(r"[*_`>#]+", "", line)
    line = re.sub(r"^\s*(?:[-+]|\d+\.)\s+", "", line)
    return re.sub(r"\s+", " ", line).strip()


def hook(text: str) -> str:
    """First line of the body that says something."""
    in_code = False
    for raw in body_of(text).splitlines():
        stripped = raw.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not stripped or stripped.startswith(("#", "|", "---", "![", "<")):
            continue
        if re.fullmatch(r"(?:[-*]\s*)?(?:!?\[\[[^\]]+\]\][,\s]*)+", stripped):
            continue  # a bare list of links is not a hook
        if re.fullmatch(r"(?:[-*]\s*)?https?://\S+", stripped):
            continue
        if re.fullmatch(r"(?:tags?:\s*)?(?:#[\w-]+\s*)+", stripped, re.IGNORECASE):
            continue  # tag line
        if re.fullmatch(r"(?:[-*]\s*)?(?:\[[^\]]*\]\([^)]*\)[,\s]*)+", stripped):
            continue  # a bare markdown link
        line = clean(stripped)
        if len(line) < 3:
            continue
        return line if len(line) <= HOOK_LEN else line[: HOOK_LEN - 1].rstrip() + "…"
    return ""


def links_in(text: str) -> list[str]:
    seen: list[str] = []
    for m in LINK_RE.finditer(body_of(text)):
        label = (m.group(2) or m.group(1)).strip()
        if label not in seen:
            seen.append(label)
    return seen


def link_name(path: Path, by_title: dict[str, set[Path]]) -> str:
    """Shortest wikilink that resolves to exactly this note."""
    candidates = [path.stem]
    title = cb.note_title(path, cb.read_text(path))
    if title:
        candidates.append(title)
    candidates.append(cb.rel(path)[:-3])
    for name in candidates:
        if cb.resolve_wiki_target(name, by_title) == [path]:
            return name
    return cb.rel(path)[:-3]


def map_label(rel_path: str) -> str:
    folder = rel_path.rsplit("/", 2)[-2]
    return {"computer-science": "Computer science map", "sanskrit-literature": "Sanskrit & philosophy map",
            "media": "Books, articles, podcasts map"}.get(folder, f"{folder} map")


def section_for(rel_path: str) -> str:
    for heading, prefix in SECTIONS:
        if rel_path.startswith(prefix):
            return heading
    return "Legacy root notes" if "/" not in rel_path else "Other"


def build() -> str:
    notes = cb.collect_notes()
    by_title = cb.title_index(notes)
    groups: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for path in notes:
        rel_path = cb.rel(path)
        if path.name in SKIP_NAMES or rel_path.startswith(SKIP_PREFIXES):
            continue
        text = cb.read_text(path)
        name = link_name(path, by_title)
        if path.name == "README.md":
            groups["Maps"].append((name, map_label(rel_path)))
        elif rel_path.startswith(JOURNAL_PREFIXES):
            groups["Log"].append((name, ""))
        elif hook(text):
            groups[section_for(rel_path)].append((name, hook(text)))
        elif links_in(text):
            groups[section_for(rel_path)].append((name, "→ " + ", ".join(links_in(text)[:4])))
        else:
            groups["Stubs to write"].append((name, ""))

    order = ["Maps"] + [h for h, _ in SECTIONS] + ["Legacy root notes", "Other", "Stubs to write", "Log"]
    total = sum(len(v) for k, v in groups.items() if k != "Log")
    out = [
        "# Index",
        "",
        "Every note, one line each: the note, then its first line.",
        "Generated by `tools/build_index.py`. Do not edit by hand.",
        "",
        f"{total} notes, plus {len(groups.get('Log', []))} journal entries under Log.",
        "",
        "Areas: " + " · ".join(f"[{h}](#{anchor(h)})" for h in order if groups.get(h)),
        "",
    ]
    for heading in order:
        items = groups.get(heading)
        if not items:
            continue
        out += [f"## {heading}", ""]
        reverse = heading == "Log"
        for name, line in sorted(items, key=lambda x: x[0].casefold(), reverse=reverse):
            out.append(f"- [[{name}]]" + (f" — {line}" if line else ""))
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def anchor(heading: str) -> str:
    slug = re.sub(r"[^\w\s-]", "", heading.lower())
    return re.sub(r"\s+", "-", slug.strip())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="fail if INDEX.md is stale")
    args = parser.parse_args()
    content = build()
    if args.check:
        current = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
        if current != content:
            print("INDEX.md is stale. Run: python3 tools/build_index.py")
            sys.exit(1)
        print("INDEX.md is current.")
        return
    INDEX.write_text(content, encoding="utf-8")
    print(f"Wrote {cb.rel(INDEX)}")


if __name__ == "__main__":
    main()
