# AGENTS.md

This repository is a personal second-brain and Zettelkasten-style note system. When creating or editing notes, optimize for durable understanding, clear links, and correct note type selection.

`RULES.md` is the source of truth for note classification. If anything here is ambiguous, follow `RULES.md` conservatively.

## Mission

- Default to evergreen, permanent notes for stable ideas that can stand on their own.
- Do not force raw captures, highlights, transcripts, or unfinished thinking into permanent notes.
- Keep the vault useful as a second brain: capture, organize, distill, and connect.

## Where New Notes Go

- Use `content/` for all new notes unless the user explicitly asks for a legacy location.
- Treat `pages/`, `journals/`, and root-level note files as legacy content. Do not create new notes there by default.
- Permanent concept notes belong in `content/domains/...` or `content/people/...`.
- Literature/source notes belong in `content/media/books/`, `content/media/books/highlights/`, `content/media/articles/`, `content/media/podcasts/`, or `content/media/videos/`.
- Research notes belong in `content/research/...`.
- Fleeting or daily capture belongs in `content/journal/`.

## Required Decision Before Writing

Every new note must be classified first:

1. `permanent`
2. `literature`
3. `research`
4. `journal`

If the note is not clearly a permanent note, do not create it as permanent.

Use this default decision logic:

- Choose `permanent` when the note explains one durable idea in your own words.
- Choose `literature` when the note is tied to a source and mainly captures what that source says.
- Choose `research` when the note contains exploration, comparisons, hypotheses, questions, or unresolved synthesis.
- Choose `journal` when the note is a fleeting capture, daily log, inbox item, or temporary observation.

## Permanent Note Standard

When creating a permanent note:

- Write in your own words.
- Keep it atomic: one core idea per note.
- Use an evergreen title based on the idea, not the source.
- Explain why the idea matters.
- Add wikilinks to related notes. Aim for at least 2 meaningful links when the context exists.
- Prefer concept titles like `Message Authentication Code` or `Identity-based habits`, not titles like `Notes from chapter 3`.
- Do not copy large quotes into permanent notes.

Permanent notes must not be:

- book highlights
- article excerpts
- raw transcripts
- meeting dumps
- brainstorming scratchpads
- unresolved research collections
- reading notes that only paraphrase one source without synthesis

## Literature Note Standard

When creating a literature note:

- Keep it attached to the source.
- Preserve quotations, highlights, timestamps, page references, or source-specific context there.
- Do not present source material as evergreen knowledge unless it has been separately distilled into a permanent note.
- Link outward to permanent notes that the source supports.

## Research Note Standard

When creating a research note:

- Treat it as a workbench, not as evergreen knowledge.
- It may contain comparisons, open questions, partial synthesis, experiments, and unresolved claims.
- Keep it in `content/research/...`.
- Do not promote it to permanent note status until the material has been distilled into self-contained idea notes.

## Journal / Fleeting Note Standard

When creating a journal note:

- Keep it in `content/journal/`.
- Use it for capture, not for final storage of knowledge.
- Promote useful ideas out of the journal into permanent notes later if they become durable and linkable.

## Frontmatter For New Notes

For new notes, keep the existing repository metadata and add `type`:

```yaml
---
title: "Note Title"
date: YYYY-MM-DD
type: permanent | literature | research | journal
category: "Domain/Subdomain"
tags: [tag1, tag2]
status: draft | incomplete | complete | archived
source: "Optional source"
related: ["[[Related Note]]"]
---
```

Notes:

- `title`, `date`, and `type` are required for new notes.
- `category`, `tags`, and `status` should be present whenever they are reasonably known.
- `source` is expected for literature and research notes tied to external material.
- `related` is strongly recommended for permanent notes.

## Promotion Rule

Only promote literature or research material into a permanent note when all of the following are true:

- the idea is durable, not merely source-bound
- it has been rewritten in your own words
- it can stand alone without the source note
- it expresses one main idea
- it connects to the existing note network

When promoting, create a new permanent note rather than silently rebranding the source or research note.

## Editing Existing Notes

- Preserve the existing note's intent and note type.
- Do not convert a literature or research note into a permanent note unless explicitly asked and the promotion rule is satisfied.
- Do not move large sets of existing notes between folders unless the user asks for migration work.
- Prefer adding links, cleanup, and synthesis over rewriting a source note into an evergreen note in place.

## Output Quality Bar

- Favor clarity over completeness.
- Prefer concise synthesis over long dumps.
- Avoid duplicate notes when a concept already exists.
- If a note idea is already covered, update the existing permanent note and add links instead of creating a near-duplicate.
