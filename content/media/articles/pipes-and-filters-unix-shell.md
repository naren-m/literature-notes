---
title: "Pipes and Filters — Unix Shell"
date: 2026-04-19
type: literature
category: "articles/tutorial"
tags: [unix, shell, bash, pipes, filters, command-line, swcarpentry, tutorial]
status: stable
source: "https://www.notion.so/77afc66bce6a44ec99e097110c07c251"
external: "https://swcarpentry.github.io/shell-novice/04-pipefilter/index.html"
related: [
  "[[linux-command-handbook]]",
  "[[find-commands]]",
  "[[cs-fundamentals-preparation-plan]]",
  "[[notion-migration]]"
]
---

# Pipes and Filters (Unix Shell)

Literature note — full-copy snapshot of the Software Carpentry "Shell Novice" Episode 4 tutorial, preserved in Notion as a standalone reference page. The page was a near-verbatim paste so the Notion copy and the online copy are equivalent; this note preserves the core conceptual content and adds local cross-links.

## Learning outcomes

- Redirect a command's output to a file with `>`
- Construct command pipelines (two or more commands connected by `|`)
- Explain Unix's philosophy of small, composable programs
- Use `wc`, `sort`, `head`, `tail`, `cat` as filters

## Core idea — programs as filters

The Unix shell treats programs as *filters*: each reads a stream of input, transforms it, and writes a stream of output. The `|` operator connects the stdout of one program to the stdin of the next, making complex queries composable from tiny tools.

> "This idea is captured in the Unix philosophy: write programs that do one thing and do it well, write programs to work together, and write programs to handle text streams, because that is a universal interface."
>
> — Doug McIlroy, via Kernighan & Pike, *The Unix Programming Environment*

## The working dataset

Examples use a `molecules` directory with files `cubane.pdb`, `ethane.pdb`, `methane.pdb`, `octane.pdb`, `pentane.pdb`, `propane.pdb` (each representing a molecule in Protein Data Bank format). Line counts vary roughly from 12 (methane) to 30 (octane).

## Counting things — `wc`

```bash
$ wc *.pdb
```

Prints three columns — lines, words, bytes — for each matched file plus a cumulative total. Flags: `-l` lines only, `-w` words only, `-c` characters only.

## Redirecting output — `>` and `>>`

```bash
$ wc -l *.pdb > lengths.txt
```

Sends stdout to the file `lengths.txt`. `>` overwrites; `>>` appends. `cat lengths.txt` reads back the contents.

## Sorting — `sort`

```bash
$ sort -n lengths.txt
```

Default is alphabetical; `-n` sorts numerically; `-r` reverses. On numeric data, always pass `-n`, otherwise `10` sorts before `9`.

## Head and tail — slicing streams

```bash
$ head -n 1 sorted-lengths.txt
$ tail -n 1 sorted-lengths.txt
```

Extract the top or bottom N lines. Legacy form `head -1 file` is deprecated — always use `-n 1`.

## Piping — the key abstraction

```bash
$ wc -l *.pdb | sort -n | head -n 1
```

Three filters chained. Each `|` connects stdout → stdin. No intermediate file required. The reader learns that any command's output can become any subsequent command's input — this is the foundation of Unix-style workflows.

## Nelle's Pipeline — the framing narrative

The tutorial follows "Nelle Nemo," a fictional marine biologist who has 1,520 data files from sampling goo-fish populations. She needs to pipeline:

1. `ls -l *[AB].txt` to list the files.
2. `goostats.sh` (provided shell script) to analyse each file.
3. `wc -l *.out` + `sort -n` to check which outputs contain the most data.

The narrative's moral: even a domain scientist with no systems background can chain five small tools into a reproducible analysis, whereas the alternative is custom Python/R that takes a week to write.

## Exercises (from the tutorial — abridged)

### What does `>>` do?

`>>` appends to a file, preserving existing content. `>` overwrites. Demonstrated with:

```bash
$ echo hello > greetings.txt
$ echo world >> greetings.txt
$ cat greetings.txt
hello
world
```

### Appending data

Combine `echo` + `>>` to grow a log file without losing history. Common in shell scripting for ad-hoc progress logs.

### Piping commands together

The question `wc -l *.pdb | sort -n` — which filename appears at the bottom of the sorted output? Answer: octane.pdb (30 lines). Teaches students to read pipeline output top-to-bottom as sorted ascending.

### Pipe reading comprehension

Given `cat animals.csv | head -n 5 | tail -n 3 | sort -r > final.txt`, students predict the contents. Lessons: head-then-tail composition extracts a middle slice; `-r` gives reverse lexicographic order; the final `> final.txt` is the only side effect.

### Pipe construction

Given a goal ("the 3 shortest .pdb files by line count"), students construct the pipeline:

```bash
$ wc -l *.pdb | sort -n | head -n 3
```

### Which pipe?

A multi-choice exercise asking which of 4 candidate pipelines achieves the goal. Tests understanding of how `head`, `tail`, `sort -r`, and `sort` interact.

### Why does `uniq` only remove adjacent duplicates?

Because `uniq` is a filter that reads its input as a stream — it has no memory beyond the previous line. To dedupe globally, pipe through `sort | uniq`.

### Pipe reading comprehension (part 2)

`sort salmon.txt | uniq` vs. `sort -u salmon.txt` — same output. Teaches `sort -u` as the idiomatic single-command version.

### Reading from stdin

`sort < animals.csv` redirects the file into sort's stdin, equivalent to `sort animals.csv`. Useful when the command doesn't accept a filename argument.

### Removing unneeded files

Students learn `rm -i` as the safer default (interactive), and that the shell's wildcard expansion happens *before* `rm` sees the arguments — so `rm *.txt` expands in place, with no way to undo.

## Takeaways (for local reference)

- **Composition over monoliths.** A ten-character pipeline can replace a ten-line script. Reach for pipelines first, scripts second.
- **Streams are universal.** Any program that reads stdin and writes stdout can be slotted into a pipeline without modification.
- **Sort is load-bearing.** Most pipelines end up using `sort -n` or `sort -u` because that is how to turn an unordered stream into a queryable one.
- **Output redirection is not pipelining.** `>` writes to a file; `|` connects stdin/stdout. Don't confuse them — `wc > sort` is broken.
- **The shell expands wildcards, not the command.** This is why `ls *.pdb` and `wc *.pdb` both "see" the same expanded filename list.

## Cross-references

- **[[linux-command-handbook]]** — fuller reference for each command (`ls`, `grep`, `find`, `sed`, `awk`) used in pipelines.
- **[[find-commands]]** — `find ... -exec ... | xargs ...` composes with pipelines.
- **[[cs-fundamentals-preparation-plan]]** — the "Tools & Shell" chapter there cites this tutorial as the baseline.
- **[[teach-yourself-computer-science]]** — the TYCS curriculum recommends Kernighan & Pike's *Unix Programming Environment* for the deeper version.

## Notes on provenance

The Notion page was titled "Pipes and Filters" (Notion ID `77afc66bce6a44ec99e097110c07c251`) and lived under the Computer Science ancestor path. Content is a copy of the Software Carpentry lesson — the external URL (https://swcarpentry.github.io/shell-novice/04-pipefilter/index.html) is the source of record and should be preferred if content diverges. This note preserves the conceptual summary rather than a verbatim re-copy; the full tutorial text is still in the Notion archive.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/77afc66bce6a44ec99e097110c07c251). See [[notion-migration]].*
