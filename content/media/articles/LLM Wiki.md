---
title: "LLM Wiki"
date: 2026-04-30
type: literature
category: "Media/Articles"
tags: [llm, knowledge-management, zettelkasten, rag, obsidian]
status: complete
source: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
related: ["[[Persistent LLM wikis make synthesis compounding]]"]
---

# LLM Wiki

Source: [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) by Andrej Karpathy. Created April 4, 2026.

## Source-bound summary

Karpathy describes a pattern for using an LLM agent to maintain a personal wiki over time. The key contrast is with ordinary RAG: a RAG system retrieves chunks from raw documents at question time, while an LLM-maintained wiki compiles what has already been learned into persistent pages. The wiki becomes an intermediate knowledge layer between raw sources and future questions.

The proposed architecture has three layers:

- raw sources: curated documents, articles, images, data files, and other evidence that should remain immutable
- the wiki: interlinked markdown pages that summarize, compare, cross-reference, and revise the accumulated understanding
- the schema: files such as `AGENTS.md`, `CLAUDE.md`, or similar instructions that tell the agent how to maintain the wiki

The main operations are ingest, query, and lint. Ingest adds a source, extracts key claims, updates related pages, and records the work. Query reads the wiki, synthesizes an answer, and may file useful answers back into the wiki. Lint periodically checks for contradictions, stale claims, orphan pages, missing links, and concepts that deserve their own page.

Karpathy also emphasizes index and log files. The index is content-oriented navigation. The log is a chronological record of ingests, queries, and maintenance. In this vault, the same idea maps naturally onto `INDEX.md`, domain README files, graphify output, and parseable entries in `content/journal/YYYY-MM-DD.md`.

## Key takeaways

- Stateless retrieval makes the LLM redo synthesis every time.
- A maintained markdown wiki lets prior synthesis compound.
- The schema file is what turns a generic agent into a disciplined wiki maintainer.
- Human attention should go toward curation, questions, review, and judgment.
- LLM attention is well suited to the tedious maintenance layer: summaries, links, consistency checks, and bookkeeping.

## Connections

- Supports [[Persistent LLM wikis make synthesis compounding]].
- Relates to [[Maintaining code base]] because the wiki is treated as a maintained artifact rather than a passive archive.
- Relates to [[Unix philosophy]] because plain markdown files, simple indexes, and parseable logs keep the system tool-friendly.
