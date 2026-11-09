# Literature Notes

Naren's second brain. Sutra-style concept notes, source notes, research workbenches, and a daily log, kept as an LLM-maintained wiki.

## Find something

1. [INDEX.md](INDEX.md): every note, one line each.
2. Maps:
   - [Computer science](content/domains/computer-science/README.md)
   - [Sanskrit & philosophy](content/domains/humanities/sanskrit-literature/README.md)
   - [Books, articles, podcasts](content/media/README.md)
3. Search:

```bash
make search q="key exchange"
```

```bash
python3 tools/search_notes.py --tag vedanta
```

## Layout

| Folder | What lives there |
|---|---|
| `content/domains/`, `content/people/` | Permanent notes: one idea each, in Naren's voice |
| `content/media/` | Literature notes: highlights, quotes, transcripts |
| `content/research/` | Workbenches: open questions, unfinished synthesis |
| `content/journal/` | Daily log and quick capture |
| `pages/`, `journals/`, root `*.md` | Legacy Logseq notes |

Rules for writing and classifying notes: [AGENTS.md](AGENTS.md) and [RULES.md](RULES.md).

## Keep it healthy

```bash
make index
```

```bash
make check
```

`make index` rebuilds `INDEX.md` (the GitHub Action also does this on every push to `main`). `make check` runs the strict backlink check and fails if `INDEX.md` is stale. `make install-hooks` adds the pre-commit backlink check.
