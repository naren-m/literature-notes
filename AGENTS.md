# AGENTS.md

This repository is a personal second-brain and Zettelkasten-style note system. When creating or editing notes, optimize for durable understanding, clear links, and correct note type selection.

`RULES.md` is the source of truth for note classification. If anything here is ambiguous, follow `RULES.md` conservatively.

A
	b
		q
		
## Owner

Read `content/people/Naren.md` before answering or writing. It says who Naren is, what he is learning, and how he wants answers.

## Mission

- Default to evergreen, permanent notes for stable ideas that can stand on their own.
- Do not force raw captures, highlights, transcripts, or unfinished thinking into permanent notes.
- Keep the vault useful as a second brain: capture, organize, distill, and connect.

## LLM Wiki Operating Model

Use this repository as a persistent, agent-maintained wiki rather than a stateless pile of retrieved files.

- Source layer: source-bound material in `content/media/...`, source assets, recordings, imported highlights, transcripts, and external URLs. Treat this material as evidence. Preserve its source context and do not rewrite it into evergreen prose in place.
- Wiki layer: distilled notes in `content/domains/...`, `content/people/...`, `content/research/...`, and `content/journal/...`. The agent may create and update these notes when doing ingestion, synthesis, cleanup, and linking.
- Schema layer: `AGENTS.md`, `RULES.md`, templates, and tooling instructions. `RULES.md` remains the source of truth for note classification.

The goal is compounding knowledge: each ingest or query should leave the vault better linked, less duplicative, and easier to query later.

## Where New Notes Go

- Use `content/` for all new notes unless the user explicitly asks for a legacy location.
- Treat `pages/`, `journals/`, and root-level note files as legacy content. Do not create new notes there by default.
- Permanent concept notes belong in `content/domains/...` or `content/people/...`.
- Literature/source notes belong in `content/media/books/`, `content/media/books/highlights/`, `content/media/articles/`, `content/media/podcasts/`, or `content/media/videos/`.
- Research notes belong in `content/research/...`.
- Fleeting or daily capture belongs in `content/journal/`.

## Inbox

- Inbox = open GitHub issues on `naren-m/literature-notes`. One issue = one capture: a URL, pasted text, or both.
- The daily compile (2:42 am Pacific) ingests each open issue with the Ingest workflow below, then opens one PR whose body has `Closes #N` for each issue, so issues close on merge.
- Can't fetch a URL (network policy, login wall, video with no transcript)? Comment on the issue with the reason and leave it open. Don't invent content.

## Core Workflows

### Ingest

When given a source, URL, transcript, book excerpt, recording, or pasted raw material:

- Classify the new material first using `RULES.md`.
- Create or update a literature, research, or journal note before extracting permanent notes.
- Preserve the source URL, author, date, timestamps, page references, or other provenance when known.
- Update existing related permanent notes instead of creating near-duplicates.
- Create a new permanent note only when one durable, standalone idea has been rewritten in your own words and can link into the existing vault.
- Add meaningful wikilinks from the source note to the distilled note and from the distilled note back to the source.
- Add a parseable activity entry to `content/journal/YYYY-MM-DD.md` using `## [YYYY-MM-DD] ingest | Source or Topic`.

### Query

When answering questions against the vault:

- Use the graph, indexes, and search to find existing notes before reading broad folders.
- Prefer answers grounded in existing note files and cite the note paths or wikilinks when useful.
- If the answer produces reusable synthesis, ask whether to file it unless the user already asked to update the vault.
- Do not treat chat-only synthesis as stored knowledge until it has been written into the right note type.

### Lint

When asked to clean up or health-check the vault, look for:

- duplicate or near-duplicate concept notes
- source-bound notes incorrectly promoted to permanent notes
- orphan notes with no meaningful inbound or outbound links
- stale claims, contradictions, broken wikilinks, and missing source provenance
- important concepts repeatedly mentioned but lacking their own permanent note

Log lint work in `content/journal/YYYY-MM-DD.md` using `## [YYYY-MM-DD] lint | Scope`.
For schema or tooling changes, use `## [YYYY-MM-DD] schema | Scope` or `## [YYYY-MM-DD] maintenance | Scope`.

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

## Writing Voice

Notes are written in Naren's voice, not in generic LLM prose.

- Use the repo skills: `.claude/skills/sutra-writing` for notes and documents, `.claude/skills/talk-like-naren` for replies. Synced from `naren-m/skills`.
- Prerequisites first: if a statement depends on an idea the vault has no note for, write that note first, then link to it. Build understanding bottom-up, from first principles.
- No ambiguity. A reader should never have to read a paragraph to get one simple point.

- Concept notes are sutra-style: the fewest words that carry the idea, one line per idea, each line worth remembering. Lead with the essence (`Nāda = Prāṇa + Agni.`, `One that sustains. What does it sustain? Balance in the creation.`), not a hedged dictionary definition.
- Article-style notes stay articles, but read like an engineer talking to a friend: short sentences, direct opinions, concrete examples, no filler.
- Keep Telugu/Sanskrit verses, verse references, open questions and TODOs verbatim.
- Do not write robotic filler: "In practical terms", "This matters because", "It is important to note", "Examples include", "Its meaning depends on", "rule of thumb", "Overview / Core Concept / Key Takeaways" sections, or `[[Link]] - one-line description` lists.
- When cleaning a note, do not flatten it into encyclopedic prose. Shorter and sharper beats complete and bland.

## Maintaining Links and Backlinks

`tools/check_backlinks.py` resolves a `[[wikilink]]` by filename stem, frontmatter `title`, or path suffix (e.g. `[[sanskrit-etymology/Rambha]]`), case-insensitively, treating `_` as a space. A link that matches no note is unresolved; a link that matches two or more notes is ambiguous.

When writing links:

- Link to a note that exists, using its real name: `[[Apsaras]]`, not `[[apsara]]`. Use `[[Target|display text]]` when the wording should differ.
- Give every new note at least one inbound link from a related existing note. A note's own outbound links do not count as backlinks.
- When a link carries a real relationship, add the reciprocal link on the target note too (its "Related" section or `related:` frontmatter).
- Do not create a second note with the same filename stem or title as an existing one, because that makes links ambiguous. If two such notes must exist, link by path.
- Do not add links to notes that do not exist as placeholders. If a concept needs a note, create it or list it as a missing concept during lint.

When moving, renaming, merging, or deleting notes:

- Use `git mv` so history follows the file.
- When moving between folders, keep the filename stem so existing links keep resolving.
- When renaming, search the vault for `[[Old Name`, the old `title`, `related:` entries, and markdown links to `Old_Name.md`, and update every one.
- When merging or deleting, point inbound links at the surviving note before removing the old one.

Verify every change:

- Run `make backlink-check` (or `python3 tools/check_backlinks.py --summary`) before and after the change. Unresolved and ambiguous counts must not go up, and permanent-note orphans must stay at 0.
- Use `make backlink-report` for a full report listing each broken, ambiguous, or orphaned link.
- The pre-commit hook (`make install-hooks`) runs the strict check on staged files. Do not bypass it with `SKIP_BACKLINK_CHECK=1` unless the user asks.

## Output Quality Bar

- Favor clarity over completeness.
- Prefer concise synthesis over long dumps.
- Avoid duplicate notes when a concept already exists.
- If a note idea is already covered, update the existing permanent note and add links instead of creating a near-duplicate.

## Finding Notes

Read in this order, cheapest first:

1. `INDEX.md`: every note, one line each, with the note's first line as a hook. Generated by `tools/build_index.py` (the GitHub Action rebuilds it on every push to `main`).
2. Map pages: `content/domains/computer-science/README.md`, `content/domains/humanities/sanskrit-literature/README.md`, `content/media/README.md`. Hand-written, sutra-style, grouped by idea.
3. Search: `python3 tools/search_notes.py <words>` (also `--tag <tag>`, `--type <type>`, `--limit N`), or `make search q="<words>"`.

Keep them useful:

- The first line of a note is its hook in the index. Make it the essence, not a definition or a link list.
- When you add a note, add it to the right map page if it belongs to a mapped area, and give it `tags`.
- After adding, renaming, or deleting notes, run `make index` (or `python3 tools/build_index.py`).
- If a `graphify-out/` graph exists, `graphify query "<question>"` can answer cross-topic questions; it is optional and not checked in.
