#!/usr/bin/env python3
"""
Backfill missing wikilinks for plain-text note title mentions.

The script treats unique Markdown file stems as note titles. For each note, it
finds unlinked mentions of other note titles and wraps the first safe occurrence
with an Obsidian/Foam-style wikilink, preserving the visible text with an alias
when casing differs.
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable, Sequence


EXCLUDED_DIRS = {
    ".codex",
    ".git",
    ".github",
    ".venv",
    "backups",
    "config",
    "graphify-out",
    "node_modules",
    "tools",
}

EXCLUDED_ROOT_FILES = {
    "AGENTS.md",
    "INDEX.md",
    "README.md",
    "RULES.md",
    "Readme.md",
}

GENERIC_TITLES = {
    "availability",
    "books",
    "confidentiality",
    "contents",
    "index",
    "india",
    "integrity",
    "music theory",
    "readme",
    "speech",
    "test",
    "title of my new note",
    "what if",
}

WIKILINK_RE = re.compile(r"\[\[([^\]\n]+)\]\]")
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]\n]*(?:\][^\[\]\n]*)*\]\([^) \n]+(?: [^)]+)?\)")
URL_RE = re.compile(r"https?://[^\s<>)]+")
INLINE_CODE_RE = re.compile(r"(?<!`)`[^`\n]+`(?!`)")


@dataclass(frozen=True)
class Note:
    path: Path
    rel_path: str
    title: str
    norm_title: str


@dataclass(frozen=True)
class Target:
    note: Note
    pattern: re.Pattern[str]


@dataclass(frozen=True)
class Change:
    file: str
    line: int
    start: int
    end: int
    target: str
    matched_text: str

    @property
    def replacement(self) -> str:
        if self.matched_text == self.target:
            return f"[[{self.target}]]"
        return f"[[{self.target}|{self.matched_text}]]"


def repo_root_from_script() -> Path:
    return Path(__file__).resolve().parents[2]


def normalize_title(title: str) -> str:
    normalized = unicodedata.normalize("NFC", title).strip()
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized.casefold()


def has_control_characters(value: str) -> bool:
    return any(unicodedata.category(char).startswith("C") for char in value)


def iter_note_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            continue
        if len(rel.parts) == 1 and rel.name in EXCLUDED_ROOT_FILES:
            continue
        yield path


def load_notes(root: Path) -> list[Note]:
    notes: list[Note] = []
    for path in iter_note_files(root):
        title = path.stem.strip()
        if not title:
            continue
        notes.append(
            Note(
                path=path,
                rel_path=path.relative_to(root).as_posix(),
                title=title,
                norm_title=normalize_title(title),
            )
        )
    return notes


def compile_title_pattern(title: str) -> re.Pattern[str]:
    escaped = re.escape(title.strip())
    escaped = escaped.replace(r"\ ", r"[ \t]+")

    left_boundary = r"(?<![\w])" if title[0].isalnum() or title[0] == "_" else ""
    right_boundary = r"(?![\w])" if title[-1].isalnum() or title[-1] == "_" else ""
    flags = 0 if is_short_acronym(title) else re.IGNORECASE
    return re.compile(f"{left_boundary}({escaped}){right_boundary}", flags)


def is_short_acronym(title: str) -> bool:
    letters = [char for char in title if char.isalpha()]
    return bool(letters) and len(title) <= 6 and all(char.isupper() for char in letters)


def build_targets(
    notes: Sequence[Note], min_title_chars: int
) -> tuple[list[Target], dict[str, list[str]]]:
    grouped: dict[str, list[Note]] = {}
    for note in notes:
        grouped.setdefault(note.norm_title, []).append(note)

    skipped: dict[str, list[str]] = {
        "duplicate": [],
        "generic": [],
        "invalid": [],
        "too_short": [],
    }
    targets: list[Target] = []

    for note in notes:
        if len(grouped[note.norm_title]) > 1:
            skipped["duplicate"].append(note.rel_path)
            continue
        if note.norm_title in GENERIC_TITLES:
            skipped["generic"].append(note.rel_path)
            continue
        if len(re.sub(r"\W+", "", note.title, flags=re.UNICODE)) < min_title_chars:
            skipped["too_short"].append(note.rel_path)
            continue
        if has_control_characters(note.title) or any(char in note.title for char in "[]|"):
            skipped["invalid"].append(note.rel_path)
            continue
        targets.append(Target(note=note, pattern=compile_title_pattern(note.title)))

    targets.sort(key=lambda target: (-len(target.note.title), target.note.title.casefold()))
    for values in skipped.values():
        values.sort()
    return targets, skipped


def merge_ranges(ranges: Iterable[tuple[int, int]]) -> list[tuple[int, int]]:
    merged: list[tuple[int, int]] = []
    for start, end in sorted(ranges):
        if start >= end:
            continue
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged


def frontmatter_range(content: str) -> tuple[int, int] | None:
    lines = content.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None

    offset = len(lines[0])
    for line in lines[1:]:
        end = offset + len(line)
        if line.strip() == "---":
            return (0, end)
        offset = end
    return None


def fenced_code_ranges(content: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    in_fence = False
    fence_char = ""
    fence_len = 0
    fence_start = 0
    offset = 0

    for line in content.splitlines(keepends=True):
        stripped = line.lstrip()
        match = re.match(r"(`{3,}|~{3,})", stripped)
        if match:
            marker = match.group(1)
            if not in_fence:
                in_fence = True
                fence_char = marker[0]
                fence_len = len(marker)
                fence_start = offset
            elif marker[0] == fence_char and len(marker) >= fence_len:
                ranges.append((fence_start, offset + len(line)))
                in_fence = False
        offset += len(line)

    if in_fence:
        ranges.append((fence_start, len(content)))
    return ranges


def heading_ranges(content: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    offset = 0
    for line in content.splitlines(keepends=True):
        if re.match(r"\s{0,3}#{1,6}\s+", line):
            ranges.append((offset, offset + len(line)))
        offset += len(line)
    return ranges


def backtick_line_ranges(content: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    offset = 0
    for line in content.splitlines(keepends=True):
        if "`" in line:
            ranges.append((offset, offset + len(line)))
        offset += len(line)
    return ranges


def protected_ranges(content: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    frontmatter = frontmatter_range(content)
    if frontmatter:
        ranges.append(frontmatter)
    ranges.extend(fenced_code_ranges(content))
    ranges.extend(heading_ranges(content))
    ranges.extend(backtick_line_ranges(content))

    for pattern in (WIKILINK_RE, MARKDOWN_LINK_RE, URL_RE, INLINE_CODE_RE):
        ranges.extend(match.span() for match in pattern.finditer(content))

    return merge_ranges(ranges)


def overlaps(start: int, end: int, ranges: Sequence[tuple[int, int]]) -> bool:
    return any(start < range_end and range_start < end for range_start, range_end in ranges)


def extract_existing_link_targets(content: str) -> set[str]:
    targets: set[str] = set()
    for match in WIKILINK_RE.finditer(content):
        raw_target = match.group(1).split("|", 1)[0].split("#", 1)[0].strip()
        if raw_target.endswith(".md"):
            raw_target = raw_target[:-3]
        raw_title = Path(raw_target).name
        if raw_title:
            targets.add(normalize_title(raw_title))
    return targets


def select_non_overlapping(candidates: Sequence[Change]) -> list[Change]:
    selected: list[Change] = []
    selected_ranges: list[tuple[int, int]] = []
    selected_targets: set[str] = set()

    ordered = sorted(candidates, key=lambda item: (-(item.end - item.start), item.start, item.target))
    for candidate in ordered:
        if candidate.target in selected_targets:
            continue
        if overlaps(candidate.start, candidate.end, selected_ranges):
            continue
        selected.append(candidate)
        selected_ranges.append((candidate.start, candidate.end))
        selected_targets.add(candidate.target)

    return sorted(selected, key=lambda item: item.start)


def find_changes_for_note(
    note: Note,
    content: str,
    targets: Sequence[Target],
    max_links_per_file: int,
) -> list[Change]:
    existing_links = extract_existing_link_targets(content)
    protected = protected_ranges(content)
    candidates: list[Change] = []

    for target in targets:
        if target.note.norm_title == note.norm_title:
            continue
        if target.note.norm_title in existing_links:
            continue

        for match in target.pattern.finditer(content):
            start, end = match.span(1)
            if overlaps(start, end, protected):
                continue

            candidates.append(
                Change(
                    file=note.rel_path,
                    line=content.count("\n", 0, start) + 1,
                    start=start,
                    end=end,
                    target=target.note.title,
                    matched_text=match.group(1),
                )
            )

    selected = select_non_overlapping(candidates)
    if max_links_per_file > 0:
        selected = selected[:max_links_per_file]
    return selected


def apply_changes(content: str, changes: Sequence[Change]) -> str:
    updated = content
    for change in sorted(changes, key=lambda item: item.start, reverse=True):
        updated = updated[: change.start] + change.replacement + updated[change.end :]
    return updated


def build_report(
    root: Path,
    dry_run: bool,
    notes: Sequence[Note],
    targets: Sequence[Target],
    skipped_targets: dict[str, list[str]],
    changes_by_file: dict[str, list[Change]],
) -> dict[str, object]:
    changes = [
        {
            "file": file,
            "line": change.line,
            "target": change.target,
            "matched_text": change.matched_text,
            "replacement": change.replacement,
        }
        for file, changes_for_file in sorted(changes_by_file.items())
        for change in changes_for_file
    ]

    return {
        "root": str(root),
        "dry_run": dry_run,
        "stats": {
            "notes_scanned": len(notes),
            "linkable_targets": len(targets),
            "files_changed": len(changes_by_file),
            "links_added": len(changes),
        },
        "skipped_targets": skipped_targets,
        "changes": changes,
    }


def default_report_path(root: Path, dry_run: bool) -> Path:
    suffix = "dry-run" if dry_run else "applied"
    return root / "graphify-out" / "link-dry-runs" / f"{date.today()}-backfill-wikilinks-{suffix}.json"


def write_report(report: dict[str, object], report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Backfill missing [[wikilinks]] where note filenames are mentioned plainly."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=repo_root_from_script(),
        help="Vault root. Defaults to the repository root inferred from this script.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write changes. Without this flag the script only reports a dry run.",
    )
    parser.add_argument(
        "--min-title-chars",
        type=int,
        default=4,
        help="Skip target filenames with fewer alphanumeric characters. Default: 4.",
    )
    parser.add_argument(
        "--max-links-per-file",
        type=int,
        default=0,
        help="Cap links added per source file. 0 means no cap. Default: 0.",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=None,
        help="Write a JSON report to this path. Defaults under graphify-out/link-dry-runs/.",
    )
    parser.add_argument(
        "--print-limit",
        type=int,
        default=80,
        help="Maximum changes to print to stdout. 0 prints all. Default: 80.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = args.root.resolve()
    dry_run = not args.apply

    notes = load_notes(root)
    targets, skipped_targets = build_targets(notes, min_title_chars=args.min_title_chars)
    changes_by_file: dict[str, list[Change]] = {}

    for note in notes:
        content = note.path.read_text(encoding="utf-8")
        changes = find_changes_for_note(
            note=note,
            content=content,
            targets=targets,
            max_links_per_file=args.max_links_per_file,
        )
        if not changes:
            continue

        changes_by_file[note.rel_path] = changes
        if not dry_run:
            note.path.write_text(apply_changes(content, changes), encoding="utf-8")

    report = build_report(
        root=root,
        dry_run=dry_run,
        notes=notes,
        targets=targets,
        skipped_targets=skipped_targets,
        changes_by_file=changes_by_file,
    )
    report_path = args.report or default_report_path(root, dry_run)
    write_report(report, report_path)

    stats = report["stats"]
    mode = "DRY RUN" if dry_run else "APPLIED"
    print(
        f"{mode}: {stats['links_added']} links across {stats['files_changed']} files "
        f"({stats['notes_scanned']} notes scanned, {stats['linkable_targets']} targets)."
    )
    print(f"Report: {report_path.relative_to(root) if report_path.is_relative_to(root) else report_path}")

    all_changes = report["changes"]
    print_limit = None if args.print_limit == 0 else args.print_limit
    for item in all_changes[:print_limit]:
        print(
            f"- {item['file']}:{item['line']} -> {item['replacement']} "
            f"(matched {item['matched_text']!r})"
        )

    if print_limit is not None and len(all_changes) > print_limit:
        print(f"... {len(all_changes) - print_limit} more changes in report")


if __name__ == "__main__":
    main()
