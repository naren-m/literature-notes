---
title: "LLM Wiki"
date: "2026-04-30"
type: "literature"
category: "Media/Articles"
tags: ["llm", "knowledge-management", "zettelkasten", "rag", "obsidian"]
status: "complete"
source: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
related: ["[[Persistent LLM wikis make synthesis compounding]]"]
---

# LLM Wiki

Source: [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) by Andrej Karpathy. Created April 4, 2026.

## Notes

- RAG = re-derive the answer from raw chunks every time. Wiki = compile once, keep it.
- Wiki is the middle layer between raw sources and future questions.
- 3 layers
  - raw sources - immutable evidence (docs, articles, images, data)
  - wiki - interlinked markdown pages, revised as understanding grows
  - schema - `AGENTS.md` / `CLAUDE.md`, tells the agent how to maintain the wiki
- 3 operations
  - ingest - add source, pull claims, update related pages, log it
  - query - read wiki, answer, file good answers back
  - lint - contradictions, stale claims, orphans, missing links, concepts needing own page
- index = navigation by content. log = chronological record of ingest / query / maintenance.
  - Here: `INDEX.md`, domain READMEs, graphify output, `content/journal/YYYY-MM-DD.md` entries.
- Schema file is what turns a generic agent into a disciplined wiki maintainer.
- Human → curation, questions, review, judgment. LLM → summaries, links, consistency, bookkeeping.

## Links

- [[Persistent LLM wikis make synthesis compounding]]
- [[Maintaining code base]] - wiki is a maintained artifact, not an archive
- [[Unix philosophy]] - plain markdown, simple indexes, parseable logs
