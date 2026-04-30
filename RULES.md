# RULES.md

These rules define how notes are classified and written in this repository so the vault behaves like a real second brain instead of a pile of markdown files.

## Core Principles

- Capture quickly, but distill before treating something as knowledge.
- Permanent notes hold durable understanding.
- Literature notes hold source-bound material.
- Research notes hold active inquiry and unfinished synthesis.
- Journal notes hold fleeting capture.
- One note should express one main idea.
- Notes should connect through wikilinks, not rely only on folder structure.
- Write notes so future-you can understand them without reopening the original source.

## Second Brain Rules

- Capture: put raw material in journal, literature, or research notes first.
- Organize: place notes by note type and domain, not by temporary convenience.
- Distill: rewrite ideas in your own words before making them permanent.
- Express: prefer notes that are reusable in writing, thinking, and connecting to other ideas.

## LLM-Maintained Wiki Rules

This vault should compound over time. LLM work should be written back into durable markdown only when it improves the vault's future usefulness.

- Keep raw or source-bound material separate from distilled knowledge.
- Treat literature notes as evidence records, not as polished evergreen claims.
- Treat research notes as workbenches for unresolved synthesis.
- Treat permanent notes as the compiled wiki layer: atomic, linkable, and understandable without reopening the source.
- Treat `AGENTS.md`, `RULES.md`, templates, and tooling docs as the schema that tells agents how to maintain the wiki.
- Do not let a convenient LLM summary erase provenance, uncertainty, or source boundaries.

Recommended operating loop:

1. Ingest source-bound material into the right non-permanent note type.
2. Distill only the durable ideas that satisfy the permanent note standard.
3. Link source notes, permanent notes, and related concepts both ways where useful.
4. Record meaningful maintenance work in `content/journal/YYYY-MM-DD.md` with headings like `## [YYYY-MM-DD] ingest | Source`, `## [YYYY-MM-DD] query | Topic`, `## [YYYY-MM-DD] lint | Scope`, or `## [YYYY-MM-DD] schema | Scope`.

## Note Types

### 1. Permanent Notes

Purpose:
- Store evergreen ideas, concepts, claims, principles, definitions, or biographies that remain useful over time.

Use a permanent note only when the note:
- contains one durable idea
- is written mostly in your own words
- can stand alone without the original source
- has a title based on the idea itself
- links to related notes

Permanent notes belong in:
- `content/domains/...`
- `content/people/...`

Permanent note titles should look like:
- `Entropy measures uncertainty`
- `Message Authentication Code`
- `Identity-based habits`

Permanent note titles should not look like:
- `Notes on Atomic Habits`
- `Research about entropy`
- `Chapter 4 summary`
- `Podcast notes`

### 2. Literature Notes

Purpose:
- Store notes tied to a specific source such as a book, article, podcast, talk, or video.

Use a literature note when the note:
- depends on a single source
- contains highlights, quotations, timestamps, or page references
- summarizes what the source says
- is still primarily source-bound rather than idea-bound

Literature notes belong in:
- `content/media/books/`
- `content/media/books/highlights/`
- `content/media/articles/`
- `content/media/podcasts/`
- `content/media/videos/`

Literature notes may link to permanent notes, but they are not permanent notes themselves.

### 3. Research Notes

Purpose:
- Store exploration, comparisons, hypotheses, drafts, question lists, open problems, and topic workbenches.

Use a research note when the note:
- is synthesizing across multiple sources but is still unfinished
- contains uncertainty, exploration, or open questions
- tracks an ongoing investigation
- would be misleading if treated as settled knowledge

Research notes belong in:
- `content/research/...`

Research notes are not permanent notes.

### 4. Journal / Fleeting Notes

Purpose:
- Capture daily thoughts, quick ideas, TODOs, observations, or temporary notes.

Journal notes belong in:
- `content/journal/`

Journal notes are inbox material. Valuable ideas can later be turned into permanent notes, but journal entries are not permanent notes.

## Hard Boundary: What Must Never Be Called A Permanent Note

Do not classify any of the following as a permanent note:

- direct book highlights
- page-by-page chapter summaries
- copied quotations without synthesis
- article excerpts
- transcript fragments
- brainstorming scratchpads
- TODO lists
- meeting notes
- active research logs
- open question collections
- speculative drafts that are not yet settled

If there is doubt, downgrade the note to `literature` or `research`.

## Promotion Rules

A literature note or research note can inspire a permanent note, but it should not simply be renamed or moved and called permanent.

Promotion is allowed only if:

1. one clear idea has been extracted
2. the idea has been rewritten in your own words
3. the note can be understood without the source material
4. the note title names the idea, not the source
5. the note links to related concepts in the vault

Recommended promotion flow:

1. Capture in literature, research, or journal note.
2. Distill the strongest single idea.
3. Create a new permanent note in the proper domain.
4. Link the permanent note back to the originating source or research note.

## Structure Rules For Permanent Notes

Permanent notes should usually include:

- a precise title
- a short statement of the core idea
- explanation in your own words
- links to related notes
- optional examples, implications, or contrasts

A good permanent note is:

- atomic
- evergreen
- linkable
- reusable
- comprehensible without rereading the source

## Metadata Rules For New Notes

For new notes, use frontmatter with at least:

```yaml
---
title: "Note Title"
date: YYYY-MM-DD
type: permanent | literature | research | journal
tags: [tag1, tag2]
status: draft | incomplete | complete | archived
---
```

Additional fields:

- `category` for domain placement
- `source` for literature and research notes
- `related` for explicit note connections

## Folder Rules

- New evergreen knowledge goes into `content/domains/...` or `content/people/...`.
- New source-bound notes go into `content/media/...`.
- New exploratory work goes into `content/research/...`.
- New fleeting capture goes into `content/journal/`.
- Do not create new notes in legacy paths such as `pages/`, `journals/`, or the repository root unless explicitly requested.

## Duplicate Prevention

Before creating a new permanent note:

- check whether the concept already exists
- if it exists, improve the existing note instead of creating a near-duplicate
- if the new note offers a distinct idea, make the distinction explicit in the title and links

## Default Rule

The system should be permanent-note oriented, but not permanent-note careless.

Default to a permanent note only when the material is already distilled and evergreen.
Otherwise capture it as literature, research, or journal material first, then promote it later if it earns that status.
