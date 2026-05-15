---
title: "Zettle (zettelkasten note template)"
date: 2020-06-29
type: research
category: "meta/note-taking"
tags: [zettelkasten, meta, note-taking]
status: seedling
source: "https://www.notion.so/1ba6eaf11e644336b91033489275d78e"
related: ["[[memory-palace]]"]
---

# Zettle

This Knowledge-DB page was a scaffold for a *zettelkasten*-style reference note in the original Notion workspace. It defined four sections and a notes view but had no captured content.

## Scaffold fields

- **Meta information** — keywords, author.
- **Brief note** — one- or two-sentence distillation.
- **Notes** — a database view pulling in related pages.
- **Backlinks** — pages that refer to this one.

## Why this matters

The zettelkasten method treats each note as an atomic, linkable idea; the scaffold above is the minimum structure needed to make a note useful weeks or years later. In this vault, the equivalent is:

- YAML frontmatter — `title`, `date`, `type`, `category`, `tags`, `source`, `related` (see `RULES.md`).
- The `related:` array and body-level `[[wikilinks]]` serve as both "notes view" and "backlinks" — Obsidian / Foam render backlinks automatically from them.

## Open threads

- Promote genuinely atomic ideas to `content/domains/` permanent notes when they earn it (per the promotion rule in `RULES.md`).
- Decide whether to keep "brief note" as a dedicated frontmatter field or let the first paragraph serve.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/1ba6eaf11e644336b91033489275d78e). See [[notion-migration]].*
