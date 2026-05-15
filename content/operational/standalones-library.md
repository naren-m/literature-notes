---
title: "Standalones Library"
date: 2026-04-19
type: index
category: "library/standalones"
tags: [standalone-pages, miscellaneous, notion-migration]
status: stable
source: "https://www.notion.so/"
related: [
  "[[notion-migration]]",
  "[[reading-library]]",
  "[[courses-library]]",
  "[[tutorials-library]]",
  "[[meeting-notes-library]]",
  "[[projects-library]]",
  "[[journal-library]]",
  "[[todo-library]]"
]
---

# Standalones library — Notion standalone pages

Consolidated index of **standalone pages** in the Notion workspace — pages that are not rows in any of the major databases (Notes, Knowledge, Resources, Courses, Tutorials, Meeting Notes, Projects, To-Do, Journal). These are hub pages, bookmark collections, or one-off captures that live at the workspace root or under area/parent pages.

## Why a library file

Most standalones are either (a) thin bookmark-only pages, (b) hub pages that embed databases (so the content is in the embedded DB, not the page itself), or (c) one-off captures that were never developed. Creating an individual markdown file per standalone would produce stubs; the two substantive standalones (**CS Fundamentals Preparation plan**, **Pipes and Filters**) got their own files. Everything else is indexed here.

## Substantive standalones (individual notes)

| Title | Notion ID | Local note |
| --- | --- | --- |
| CS Fundamentals Preparation plan | `9dab6c2ff09e4d2788ac33d131427746` | [[cs-fundamentals-preparation-plan]] |
| Pipes and Filters (Unix Shell) | `77afc66bce6a44ec99e097110c07c251` | [[pipes-and-filters-unix-shell]] |

## Hub pages (embed DBs — content is elsewhere)

| Title | Notion ID | What it embeds | Where content lives |
| --- | --- | --- | --- |
| Reading List | `02e8e266e7304dfb8f4e14ec88bcaf29` | Reading DB view | [[reading-library]] |
| Mathematics | `f5595ee88f764a81898a319e8b1edb9d` | Cambridge reading list bookmark + Fermat / Flatland book mentions | [[reading-library]] (books) + `content/domains/mathematics/` |
| Computer Science (area) | *(parent area)* | Knowledge DB subset (CS pages) | [[notion-migration]] — CS subset |
| YouTube (area) | *(parent area)* | Tutorials DB + YouTube Videos project | [[tutorials-library]] + [[projects-library]] |
| Personal (area) | `bb3c23845ac14d8fa8164b387d40941e` | Journal + Home/Sahasra projects | [[journal-library]] + [[projects-library]] |
| Areas | *(parent)* | Category hub pointing at the above | *(structural — not a note)* |

## Thin / bookmark-only pages

Pages with 1–3 bookmarks or 1–3 bullet points of content; preserved here as rows rather than individual stub files.

| Title | Notion ID | Kind | Notes |
| --- | --- | --- | --- |
| Measure distance earth-moon | `ff00f0c7ae7f467e80818e1a935e188a` | Curiosity capture | 3 bullet questions + 2 bookmarks on parallax and laser-ranging |
| Linux Command Handbook | *(listed)* | Bookmark | External freeCodeCamp reference |
| Find Commands | *(listed)* | Bookmark | `find` flag cheatsheet |
| Cat6 Cables | *(listed)* | Bookmark | Home networking purchase notes |
| Luke-Poeppel / decitala | *(listed)* | Bookmark | GitHub link, carnatic-rhythm analysis tool |
| Algorithms and DS (hub) | `54c766c1b6d14c7b8a00d00fde6ccdf6` | Hub | Embeds Knowledge DB view filtered to algorithms |
| Master Algorithms & Data Structures | `169ef5d80fb04eb9aad75c3baaac7f06` | Project hub | Points at [[mit-6006-introduction-to-algorithms]]; see [[projects-library]] |

## Notion reference page (cross-linked)

The **Notion reference** standalone (`348bc7a0d8dc810bbd91d69f77a00fdc`) was the original "how this workspace is organized" doc. It is the Notion-side companion to [[notion-migration]] and lists the databases by area. No separate migration file — this whole literature vault *is* its migration.

## Totals

- Substantive standalones (individual notes): 2
- Hub pages (embed DBs): 6
- Thin / bookmark-only pages: ~7
- **Total enumerated: ~15 standalone pages**

The long tail of truly tiny standalones (one-line scratch pages, Notion-UX templates, accidentally-created pages) was not individually enumerated — Notion search surfaced the content-bearing ones, and the rest can be pruned at deprovisioning time.

## Cross-references

- **[[notion-migration]]** — master migration hub covering Notes + Knowledge DBs.
- **[[reading-library]]** — reading-list hub content lives here.
- **[[projects-library]]** — project-hub pages are indexed there.
- **[[journal-library]]** — Personal area content is there.
- **[[cs-fundamentals-preparation-plan]]** — extracted substantive standalone.
- **[[pipes-and-filters-unix-shell]]** — extracted substantive standalone.

## Open threads

- The thin bookmark pages (Cat6 Cables, Linux Command Handbook, Find Commands) are small enough that if any of them gets actually referenced from another note, the right move is to promote it to a `content/media/articles/<slug>.md` on demand. Until then, the row in this index is sufficient.
- The Luke-Poeppel / decitala bookmark is the only entry that touches the Carnatic-rhythm / Sanskrit-poetics research thread — cross-link it from `content/domains/humanities/` if that area ever grows a research note.
- The Mathematics hub is under-developed — worth a later sweep to pull its Cambridge reading-list bookmark into a proper `content/domains/mathematics/cambridge-reading-list.md` literature note if the list matters.

---

*Migrated from Notion on 2026-04-19. See [[notion-migration]].*
