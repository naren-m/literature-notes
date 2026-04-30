---
title: "Persistent LLM wikis make synthesis compounding"
date: 2026-04-30
type: permanent
category: "Computer Science/Knowledge Management"
tags: [llm, knowledge-management, zettelkasten, rag]
status: draft
source: "[[LLM Wiki]]"
related: ["[[LLM Wiki]]", "[[Unix philosophy]]", "[[Maintaining code base]]"]
---

# Persistent LLM wikis make synthesis compounding

An LLM becomes more useful as a knowledge partner when its work is written into a persistent wiki instead of disappearing into chat history or being recomputed from raw documents on every question.

In a pure retrieval workflow, each answer starts almost from zero. The system searches source material, extracts relevant fragments, and assembles a response for the immediate prompt. That can answer the current question, but the structure discovered during the answer is not necessarily preserved. The next subtle question may require the same synthesis again.

A maintained wiki changes the unit of accumulation. Sources still matter as evidence, but the reusable product is an interlinked set of notes: concepts, entities, comparisons, contradictions, summaries, and open questions. Each ingest can update the compiled layer. Each useful query can become a new note or improve an existing one. The knowledge base therefore becomes easier to navigate over time rather than merely larger.

This matters because the hard part of a personal knowledge system is usually maintenance, not storage. Cross-references, provenance, duplicate prevention, and stale-claim cleanup are exactly the kinds of bookkeeping that people often avoid and LLM agents can perform consistently when given a clear schema.

The practical constraint is note type discipline. Source-bound material should stay in literature notes, unresolved exploration should stay in research notes, and only distilled ideas should become permanent notes. Without that boundary, the wiki grows quickly but becomes less trustworthy.

## Related

- [[LLM Wiki]]
- [[Unix philosophy]]
- [[Maintaining code base]]
