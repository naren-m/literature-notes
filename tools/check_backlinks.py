#!/usr/bin/env python3
"""Check wiki-link health and backlink coverage for the literature notes vault."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "INDEX.md"

SKIP_DIRS = {
    ".codex",
    ".git",
    ".mypy_cache",
    ".serena",
    ".venv",
    "__pycache__",
    "assets",
    "config",
    "graphify-out",
    "node_modules",
    "reports",
}

SKIP_FILES = {
    "AGENTS.md",
    "INDEX.md",
    "RULES.md",
    "Readme.md",
}

PERMANENT_PREFIXES = (
    "content/domains/",
    "content/people/",
)

NON_PERMANENT_TYPES = {
    "journal",
    "literature",
    "research",
}

WIKI_LINK_RE = re.compile(r"!?\[\[([^\]\n]+)\]\]")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*", re.DOTALL)
TITLE_RE = re.compile(r"(?m)^title:\s*[\"']?([^\"'\n]+)[\"']?\s*$")
TYPE_RE = re.compile(r"(?m)^type:\s*([A-Za-z_-]+)\s*$")
HEADING_RE = re.compile(r"(?m)^#\s+(.+?)\s*$")


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def should_skip(path: Path) -> bool:
    rel_path = rel(path)
    if rel_path in SKIP_FILES:
        return True

    parts = rel_path.split("/")
    return any("/".join(parts[:idx]) in SKIP_DIRS for idx in range(1, len(parts) + 1))


def collect_notes() -> list[Path]:
    return sorted(path.resolve() for path in ROOT.rglob("*.md") if not should_skip(path.resolve()))


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ""


def normalize_title(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("_", " ")).strip().casefold()


def frontmatter_value(text: str, pattern: re.Pattern[str]) -> str | None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    value = pattern.search(match.group(1))
    return value.group(1).strip() if value else None


def note_title(path: Path, text: str) -> str | None:
    title = frontmatter_value(text, TITLE_RE)
    if title:
        return title

    heading = HEADING_RE.search(text)
    return heading.group(1).strip() if heading else None


def add_title_key(index: dict[str, set[Path]], key: str, path: Path) -> None:
    key = key.strip()
    if not key:
        return
    index[key].add(path)
    index[normalize_title(key)].add(path)


def title_index(notes: list[Path]) -> dict[str, set[Path]]:
    by_title: dict[str, set[Path]] = defaultdict(set)
    for path in notes:
        text = read_text(path)
        rel_without_suffix = rel(path)[:-3]
        add_title_key(by_title, path.stem, path)
        add_title_key(by_title, rel_without_suffix, path)

        title = note_title(path, text)
        if title:
            add_title_key(by_title, title, path)

        parts = rel_without_suffix.split("/")
        for idx in range(1, len(parts)):
            add_title_key(by_title, "/".join(parts[idx:]), path)

    return by_title


def wiki_target(raw: str) -> str:
    return raw.split("|", 1)[0].split("#", 1)[0].strip()


def resolve_wiki_target(target: str, by_title: dict[str, set[Path]]) -> list[Path]:
    candidates: set[Path] = set()
    for key in (target, normalize_title(target)):
        candidates.update(by_title.get(key, set()))

    if not candidates and target:
        direct = (ROOT / target).with_suffix(".md").resolve()
        if direct.exists() and not should_skip(direct):
            candidates.add(direct)

    return sorted(candidates)


def local_markdown_target(source: Path, raw_target: str) -> Path | None:
    parsed = urlparse(raw_target.strip())
    if parsed.scheme or parsed.netloc:
        return None

    target = unquote(parsed.path)
    if not target or not target.endswith(".md"):
        return None

    return (source.parent / target).resolve()


def index_references(notes: list[Path], by_title: dict[str, set[Path]]) -> tuple[set[Path], set[str], set[str]]:
    refs: set[Path] = set()
    stale: set[str] = set()
    ambiguous: set[str] = set()
    text = read_text(INDEX)
    note_set = set(notes)

    for match in WIKI_LINK_RE.finditer(text):
        target = wiki_target(match.group(1))
        if not target:
            continue
        candidates = resolve_wiki_target(target, by_title)
        if len(candidates) == 1:
            refs.add(candidates[0])
        elif len(candidates) > 1:
            ambiguous.add(target)
        else:
            stale.add(target)

    for match in MARKDOWN_LINK_RE.finditer(text):
        target = local_markdown_target(INDEX, match.group(1))
        if target and target in note_set:
            refs.add(target)
        elif target:
            stale.add(match.group(1))

    return refs, stale, ambiguous


def collect_link_state(
    notes: list[Path],
) -> tuple[dict[Path, set[Path]], dict[Path, set[Path]], dict[str, set[Path]], dict[str, set[Path]]]:
    by_title = title_index(notes)
    note_set = set(notes)
    inbound: dict[Path, set[Path]] = defaultdict(set)
    outbound: dict[Path, set[Path]] = defaultdict(set)
    broken: dict[str, set[Path]] = defaultdict(set)
    ambiguous: dict[str, set[Path]] = defaultdict(set)

    for source in notes:
        text = read_text(source)

        for match in WIKI_LINK_RE.finditer(text):
            target = wiki_target(match.group(1))
            if not target:
                continue
            candidates = resolve_wiki_target(target, by_title)
            if len(candidates) == 1:
                destination = candidates[0]
                if destination != source:
                    inbound[destination].add(source)
                    outbound[source].add(destination)
            elif len(candidates) > 1:
                ambiguous[target].add(source)
            else:
                broken[target].add(source)

        for match in MARKDOWN_LINK_RE.finditer(text):
            target = local_markdown_target(source, match.group(1))
            if target and target in note_set and target != source:
                inbound[target].add(source)
                outbound[source].add(target)

    return inbound, outbound, broken, ambiguous


def note_type(path: Path) -> str | None:
    value = frontmatter_value(read_text(path), TYPE_RE)
    return value.casefold() if value else None


def is_permanent_candidate(path: Path) -> bool:
    rel_path = rel(path)
    if path.name.lower() == "readme.md":
        return False
    if not rel_path.startswith(PERMANENT_PREFIXES):
        return False
    return note_type(path) not in NON_PERMANENT_TYPES


def backlink_orphans(notes: list[Path], inbound: dict[Path, set[Path]]) -> list[Path]:
    return [path for path in notes if is_permanent_candidate(path) and path not in inbound]


def isolated_notes(notes: list[Path], inbound: dict[Path, set[Path]], outbound: dict[Path, set[Path]]) -> list[Path]:
    return [
        path
        for path in notes
        if is_permanent_candidate(path) and path not in inbound and path not in outbound
    ]


def format_sources(paths: set[Path], limit: int = 6) -> str:
    names = sorted(rel(path) for path in paths)
    shown = ", ".join(f"`{name}`" for name in names[:limit])
    if len(names) > limit:
        shown += f", +{len(names) - limit} more"
    return shown


def staged_markdown_paths() -> set[Path]:
    try:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return set()

    paths: set[Path] = set()
    for line in result.stdout.splitlines():
        if line.endswith(".md"):
            path = (ROOT / line).resolve()
            if path.exists() and not should_skip(path):
                paths.add(path)
    return paths


def collect_report_state(strict_scope: set[Path] | None = None) -> dict[str, object]:
    notes = collect_notes()
    by_title = title_index(notes)
    index_refs, stale_index_refs, ambiguous_index_refs = index_references(notes, by_title)
    inbound, outbound, broken, ambiguous = collect_link_state(notes)
    orphans = backlink_orphans(notes, inbound)
    isolated = isolated_notes(notes, inbound, outbound)
    strict_orphans = [path for path in orphans if strict_scope is None or path in strict_scope]
    return {
        "notes": notes,
        "missing_from_index": [path for path in notes if path not in index_refs],
        "stale_index_refs": stale_index_refs,
        "ambiguous_index_refs": ambiguous_index_refs,
        "broken": broken,
        "ambiguous": ambiguous,
        "orphans": orphans,
        "isolated": isolated,
        "strict_orphans": strict_orphans,
    }


def render_report(state: dict[str, object]) -> str:
    notes = state["notes"]
    missing_from_index = state["missing_from_index"]
    stale_index_refs = state["stale_index_refs"]
    ambiguous_index_refs = state["ambiguous_index_refs"]
    broken = state["broken"]
    ambiguous = state["ambiguous"]
    orphans = state["orphans"]
    isolated = state["isolated"]

    lines = [
        "# Backlink Lint",
        "",
        f"Date: {dt.date.today().isoformat()}",
        "",
        "Scope: markdown notes in the vault, excluding generated/config/assets directories. Strict backlink coverage is focused on permanent-note candidates under `content/domains/` and `content/people/`.",
        "",
        "## Summary",
        "",
        f"- Notes scanned: {len(notes)}",
        f"- Notes missing from `INDEX.md`: {len(missing_from_index)}",
        f"- Unresolved `INDEX.md` targets: {len(stale_index_refs)}",
        f"- Ambiguous `INDEX.md` targets: {len(ambiguous_index_refs)}",
        f"- Unresolved wiki-link targets: {len(broken)}",
        f"- Ambiguous wiki-link targets: {len(ambiguous)}",
        f"- Permanent-note candidates with no inbound semantic links: {len(orphans)}",
        f"- Permanent-note candidates with no inbound or outbound semantic links: {len(isolated)}",
        "",
        "## Index Coverage",
        "",
    ]

    if missing_from_index:
        lines.append("These notes are not currently referenced by `INDEX.md`:")
        lines.append("")
        lines.extend(f"- `{rel(path)}`" for path in missing_from_index)
    else:
        lines.append("All scanned notes are referenced by `INDEX.md`.")

    if stale_index_refs:
        lines.extend(["", "Unresolved targets currently present in `INDEX.md`:", ""])
        lines.extend(f"- `{target}`" for target in sorted(stale_index_refs, key=str.casefold))

    if ambiguous_index_refs:
        lines.extend(["", "Ambiguous targets currently present in `INDEX.md`:", ""])
        lines.extend(f"- `{target}`" for target in sorted(ambiguous_index_refs, key=str.casefold))

    lines.extend(["", "## Unresolved Wiki Links", ""])
    if broken:
        lines.append("These wiki-link targets do not resolve to a scanned note:")
        lines.append("")
        for target, sources in sorted(broken.items(), key=lambda item: (-len(item[1]), item[0].casefold())):
            lines.append(f"- target `{target}` from {format_sources(sources)}")
    else:
        lines.append("No unresolved wiki-link targets found.")

    lines.extend(["", "## Ambiguous Wiki Links", ""])
    if ambiguous:
        lines.append("These targets match more than one note and should be disambiguated by path or alias:")
        lines.append("")
        for target, sources in sorted(ambiguous.items(), key=lambda item: item[0].casefold()):
            lines.append(f"- target `{target}` from {format_sources(sources)}")
    else:
        lines.append("No ambiguous wiki-link targets found.")

    lines.extend(["", "## Missing Backlinks", ""])
    if orphans:
        lines.append("These permanent-note candidates have no inbound note-to-note link:")
        lines.append("")
        lines.extend(f"- `{rel(path)}`" for path in orphans)
    else:
        lines.append("No permanent-note backlink orphans found.")

    lines.extend(["", "## Isolated Permanent Notes", ""])
    if isolated:
        lines.append("These permanent-note candidates have neither inbound nor outbound note-to-note links:")
        lines.append("")
        lines.extend(f"- `{rel(path)}`" for path in isolated)
    else:
        lines.append("No isolated permanent-note candidates found.")

    return "\n".join(lines).rstrip() + "\n"


def render_summary(state: dict[str, object], staged: bool) -> str:
    notes = state["notes"]
    missing_from_index = state["missing_from_index"]
    stale_index_refs = state["stale_index_refs"]
    ambiguous_index_refs = state["ambiguous_index_refs"]
    broken = state["broken"]
    ambiguous = state["ambiguous"]
    orphans = state["orphans"]
    isolated = state["isolated"]
    strict_orphans = state["strict_orphans"]

    scope = "staged permanent-note candidates" if staged else "all permanent-note candidates"
    lines = [
        "Backlink check summary:",
        f"- Notes scanned: {len(notes)}",
        f"- Notes missing from INDEX.md: {len(missing_from_index)}",
        f"- Unresolved INDEX.md targets: {len(stale_index_refs)}",
        f"- Ambiguous INDEX.md targets: {len(ambiguous_index_refs)}",
        f"- Unresolved wiki-link targets: {len(broken)}",
        f"- Ambiguous wiki-link targets: {len(ambiguous)}",
        f"- Permanent-note backlink orphans: {len(orphans)}",
        f"- Isolated permanent-note candidates: {len(isolated)}",
        f"- Strict scope: {scope}",
    ]

    if strict_orphans:
        lines.extend(["", "Missing inbound links in strict scope:"])
        lines.extend(f"- {rel(path)}" for path in strict_orphans[:20])
        if len(strict_orphans) > 20:
            lines.append(f"- ... +{len(strict_orphans) - 20} more")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", type=Path, help="Write the report to this path relative to the repository root.")
    parser.add_argument("--summary", action="store_true", help="Print only a short summary.")
    parser.add_argument("--staged", action="store_true", help="Limit strict backlink failures to staged markdown files.")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when strict-scope permanent notes have no inbound links.")
    args = parser.parse_args()

    strict_scope = staged_markdown_paths() if args.staged else None
    state = collect_report_state(strict_scope)
    report = render_report(state)
    if args.write:
        destination = args.write
        if not destination.is_absolute():
            destination = ROOT / destination
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(report, encoding="utf-8")
        print(f"Updated {rel(destination)}")
    elif args.summary:
        print(render_summary(state, args.staged), end="")
    else:
        print(report, end="")

    if args.strict and state["strict_orphans"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
