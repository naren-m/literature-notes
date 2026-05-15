---
title: "Notion Migration Hub"
date: 2026-04-19
type: research
category: "meta/migration"
tags: [migration, notion, meta]
status: complete
source: "Notion workspace (full — all databases and standalone pages)"
related: [
  "[[reading-library]]",
  "[[courses-library]]",
  "[[tutorials-library]]",
  "[[meeting-notes-library]]",
  "[[projects-library]]",
  "[[journal-library]]",
  "[[todo-library]]",
  "[[standalones-library]]",
  "[[additional-content-library]]"
]
---

# Notion Migration Hub

Tracking migration of content from the Notion "second brain" into this markdown vault. The goal is to leave Notion and rely on pure markdown under `content/`.

## Scope

- **First phase:** Notion databases **Notes** (`0e2ad108-a022-4262-9a51-0530664538a2`) and **Knowledge** (`42d23e3e-3c77-4d15-9a90-62a97c30bc42`) — 55 pages, all migrated (detail tables below).
- **Second phase (2026-04-19):** full-workspace sweep of the remaining databases — **Resources**, **Courses**, **Tutorials**, **Meeting Notes**, **Projects**, **To-Do**, **Journal** — plus standalone pages. These databases are dominated by operational ephemera and bookmark-only stubs; they are captured via **consolidated library index files** with individual notes written only for content-rich pages. See [Phase 2 libraries](#phase-2-libraries) below.
- Classification follows `RULES.md`. Source-bound material became literature notes in `content/media/...`; exploratory concept stubs became research notes in `content/research/...`; operational ephemera (tasks, meetings, projects, journal entries) live in consolidated indexes under `content/operational/`.
- Permanent notes were **not** auto-created during migration. Any permanent note requires manual promotion per the promotion rule in `RULES.md`.

## Status: complete (2026-04-19)

**Phase 1** — all **55** pages from the Notes + Knowledge databases have been migrated. This total reflects a second sweep on 2026-04-19 that caught 16 pages missed in the first pass (see [Completion sweep](#completion-sweep-2026-04-19) below).

**Phase 2** — the Resources, Courses, Tutorials, Meeting Notes, Projects, To-Do, Journal databases and standalone pages have been indexed via eight consolidated library files (see [Phase 2 libraries](#phase-2-libraries)). Content-rich pages within those databases received individual literature notes; bookmark-only / operational-ephemera pages are indexed rather than individually migrated.

Each migrated file embeds its own Notion URL in frontmatter (`source:`) and in a footer link back to the original page, so provenance is preserved even outside this hub.

## Migration conventions

- Each migrated note carries `source` in frontmatter pointing back to the original Notion URL, so provenance is never lost.
- Notion-internal links (`notion.so/<id>`) that appear inside body text were preserved as-is; they can be rewritten to wikilinks in a later pass once their targets are migrated too.
- Empty or near-empty Notion pages became **research stubs** rather than literature notes — short but useful starter notes on the concept, with "Open threads" for follow-up.
- Book / article / video / podcast notes go in `content/media/{books|articles|videos|podcasts}/` based on the Notion `Type` property.
- One title correction: the Notion page "Warm Holes" was a typo for **Wormholes** and was migrated under the corrected title.

## Pilot batch (reviewed and approved)

Five representative pages converted to markdown first for review. User approved the pilot and requested "migrate everything now; create research stubs (same as pilot)" for empty pages.

| Notion page | Local note | Type | Notion ID |
| --- | --- | --- | --- |
| Clean Code 1 | [[clean-code-lesson-1]] | literature (video) | [4920af3d4dea4886b89a4aaaacea45c4](https://www.notion.so/4920af3d4dea4886b89a4aaaacea45c4) |
| Solve interval based problems | [[solve-interval-based-problems]] | literature (article) | [c4e4688a2e8949bcbbde41ac512018b2](https://www.notion.so/c4e4688a2e8949bcbbde41ac512018b2) |
| Habit | [[habit-formation-stages]] | literature (article) | [2af859c22ad048cf9a5e22a39129d675](https://www.notion.so/2af859c22ad048cf9a5e22a39129d675) |
| Quantum Entanglement | [[quantum-entanglement]] | research (stub) | [53e48b1ea64b4b1bb8f7544a86360e10](https://www.notion.so/53e48b1ea64b4b1bb8f7544a86360e10) |
| Resurrecting Duckling model | [[resurrecting-duckling-model]] | research | [8547058e4ebb4446b4468a1367239211](https://www.notion.so/8547058e4ebb4446b4468a1367239211) |

## Literature notes

### Articles — `content/media/articles/`

| Notion page | Local note | Notion ID |
| --- | --- | --- |
| Solve interval based problems | [[solve-interval-based-problems]] | [c4e4688a2e8949bcbbde41ac512018b2](https://www.notion.so/c4e4688a2e8949bcbbde41ac512018b2) |
| Habit | [[habit-formation-stages]] | [2af859c22ad048cf9a5e22a39129d675](https://www.notion.so/2af859c22ad048cf9a5e22a39129d675) |
| Algodeck — algorithm flashcards | [[algodeck-algorithm-flashcards]] | [d49fc91ac638468393399fd2d4edc9ae](https://www.notion.so/d49fc91ac638468393399fd2d4edc9ae) |
| GPU passthrough on Proxmox (r/homelab) | [[gpu-passthrough-proxmox-guide]] | [2240a3646ae04a89bf418491f73f2c74](https://www.notion.so/2240a3646ae04a89bf418491f73f2c74) |
| Subhashitani | [[subhashitani]] | [1f155991d0574be7888f5898127207fa](https://www.notion.so/1f155991d0574be7888f5898127207fa) |
| Sanskrit Dictionaries (OneTab) | [[sanskrit-dictionaries]] | [f77fc21084254751bd7684b44c94634b](https://www.notion.so/f77fc21084254751bd7684b44c94634b) |
| Harmonic Series (UCSC PDF) | [[harmonic-series]] | [e3935f78f50847b395f727f6246d8dad](https://www.notion.so/e3935f78f50847b395f727f6246d8dad) |
| Generating Functions — Brilliant | [[generating-functions-brilliant]] | [a44a40787bdd4510b0ed664105999744](https://www.notion.so/a44a40787bdd4510b0ed664105999744) |
| Markdown Diagrams (GitHub gist) | [[markdown-diagrams]] | [e4997fbd702548bfae279a0c94bcadeb](https://www.notion.so/e4997fbd702548bfae279a0c94bcadeb) |
| How to Publish Your Own Python Package on PyPi | [[How to Publish Your Own Python Package on PyPi]] | *(pre-existing in vault)* |
| Machine Learning Is Fun Part 4 — Face Recognition | [[Machine Learning Is Fun Part 4 Modern Face Recognition With Deep Learning]] | *(pre-existing in vault)* |
| RFC 7950 — YANG 1.1 Data Modeling Language | [[RFC 7950 - The YANG 1.1 Data Modeling Language]] | *(pre-existing in vault)* |
| RFC 1831 | [[Rfc1831]] | *(pre-existing in vault)* |
| RFC 793 | [[Rfc793]] | *(pre-existing in vault)* |

### Videos — `content/media/videos/`

| Notion page | Local note | Notion ID |
| --- | --- | --- |
| Clean Code 1 | [[clean-code-lesson-1]] | [4920af3d4dea4886b89a4aaaacea45c4](https://www.notion.so/4920af3d4dea4886b89a4aaaacea45c4) |
| Analyzing "find max" algorithm | [[analyzing-find-max-algorithm]] | [0f7a260c6a534f008d061f0ac83e300f](https://www.notion.so/0f7a260c6a534f008d061f0ac83e300f) |
| Four Forces of the Universe (Michio Kaku) | [[four-forces-of-the-universe-kaku]] | [f888f680cf4b461c866b74ee63cbf6dd](https://www.notion.so/f888f680cf4b461c866b74ee63cbf6dd) |
| Folding skills (Instagram reel) | [[folding-skills]] | [e888939c7c184e4e9801826885d01d72](https://www.notion.so/e888939c7c184e4e9801826885d01d72) |
| Realtime note detection (rtmonoaudio2midi) | [[realtime-note-detection]] | [0eafa0e1ce8742828d6097f50b80eb02](https://www.notion.so/0eafa0e1ce8742828d6097f50b80eb02) |
| Sangam — History of Indian Science | [[sangam_history_of_indian_science]] | *(pre-existing in vault)* |

### Podcasts — `content/media/podcasts/`

| Notion page | Local note | Notion ID |
| --- | --- | --- |
| India Before Invasions (Sandeep Balakrishna) | [[India Before Invasions - Explained By Sandeep Balakrishna]] | *(pre-existing in vault)* |
| Jyothisha & Rajvedam (BeerBiceps) | [[jyothisha_rajvedam_beerbiceps]] | *(pre-existing in vault)* |

### Books — `content/media/books/`

| Notion page | Local note | Notion ID |
| --- | --- | --- |
| Ashtanga Hrdayam | [[AshtangaHrydayam]] | *(pre-existing in vault)* |
| Books (hub) | [[Books]] | *(pre-existing in vault)* |
| Early Indians | [[Early Indians]] | *(pre-existing in vault)* |
| Maharana Bappa Rawal | [[Maharana Bappa Rawal]] | *(pre-existing in vault)* |
| Navneetakam | [[Navneetakam]] | *(pre-existing in vault)* |
| Ranveer Show — Indian Archaeologist | [[RanveerShow-Indain Archaeologist]] | *(pre-existing in vault)* |
| Sutrasthana | [[Suthrasthana]] | *(pre-existing in vault)* |

## Research notes — `content/research/`

### Algorithms and data structures

| Notion page | Local note | Notion ID |
| --- | --- | --- |
| Data Structures & Algorithms (hub) | [[data-structures-and-algorithms]] | [ebab0d8fd69f43bd9c237af0ea200103](https://www.notion.so/ebab0d8fd69f43bd9c237af0ea200103) |
| Sorting | [[sorting]] | [c1d5560d94494a63bbef04a2ce91b9f5](https://www.notion.so/c1d5560d94494a63bbef04a2ce91b9f5) |
| Merge sort | [[merge-sort]] | [ce4168d49acc41f08d1a1fbcf0060e09](https://www.notion.so/ce4168d49acc41f08d1a1fbcf0060e09) |
| Quick sort | [[quick-sort]] | [ed0884a24f5447d0beb3089c289d65ac](https://www.notion.so/ed0884a24f5447d0beb3089c289d65ac) |
| Insertion sort | [[insertion-sort]] | [dc86ce034bf04be59650ff05b9448d16](https://www.notion.so/dc86ce034bf04be59650ff05b9448d16) |
| Heapsort | [[heapsort]] | [162d6ccdd9104732b2ef59feef9b007c](https://www.notion.so/162d6ccdd9104732b2ef59feef9b007c) |
| Counting sort | [[counting-sort]] | [fad526f3a26f414b8bdb7d7427cfad7f](https://www.notion.so/fad526f3a26f414b8bdb7d7427cfad7f) |
| Radix sort | [[radix-sort]] | [05f74ac7a4ee4979b952c622726a7915](https://www.notion.so/05f74ac7a4ee4979b952c622726a7915) |
| Hashing | [[hashing]] | [161c49b4057e480ea3a99bf1ceb960d5](https://www.notion.so/161c49b4057e480ea3a99bf1ceb960d5) |
| Trees | [[trees]] | [e466feb7fa8a4f06bffe154c8c1ea9cb](https://www.notion.so/e466feb7fa8a4f06bffe154c8c1ea9cb) |
| Trees — Q&A PDF stub | [[trees-qa]] | [9db8f52b14a148beb800a531ed903e20](https://www.notion.so/9db8f52b14a148beb800a531ed903e20) |
| Binary search tree | [[binary-search-tree]] | [99afcda3d01c4f08a399c580cdb43cb3](https://www.notion.so/99afcda3d01c4f08a399c580cdb43cb3) |
| AVL trees | [[avl-trees]] | [5683ff4f1b5948fb9e5be5d45486e45f](https://www.notion.so/5683ff4f1b5948fb9e5be5d45486e45f) |
| Heap data structure | [[heap-data-structure]] | [1d34aa4b3ffb4fb7ae66eb5c3672d3b1](https://www.notion.so/1d34aa4b3ffb4fb7ae66eb5c3672d3b1) |
| Asymptotic notations | [[asymptotic-notations]] | [8a7cc4ce05414cf4b553de2c648d87cb](https://www.notion.so/8a7cc4ce05414cf4b553de2c648d87cb) |
| Divide and conquer | [[divide-and-conquer]] | [442e52ad49274d9cb287084d493a3858](https://www.notion.so/442e52ad49274d9cb287084d493a3858) |
| Recursion | [[recursion]] | [11819799344c46d6bd7e70464643cbc9](https://www.notion.so/11819799344c46d6bd7e70464643cbc9) |
| Outlining the problem | [[outlining-the-problem]] | [a738876f66a04bfe9f8475772fcd7bb4](https://www.notion.so/a738876f66a04bfe9f8475772fcd7bb4) |
| Facebook compression problem *(stub)* | [[facebook-compression-problem]] | [17af27cd697f4edaa3060143f6868ac6](https://www.notion.so/17af27cd697f4edaa3060143f6868ac6) |

### Math

| Notion page | Local note | Notion ID |
| --- | --- | --- |
| Logarithms | [[logarithms]] | [c64d464def104ed08ae949956e86b962](https://www.notion.so/c64d464def104ed08ae949956e86b962) |
| Exponents | [[exponents]] | [62e380df816349ba8ab1010cf261bdfe](https://www.notion.so/62e380df816349ba8ab1010cf261bdfe) |
| Generating Functions | [[generating-functions]] | [fd4e71e171844053a106a4f8b3689e20](https://www.notion.so/fd4e71e171844053a106a4f8b3689e20) |
| Number theory practicals | [[number-theory-practicals]] | [0aeea30c5cdb40f5bcda37782c078c6e](https://www.notion.so/0aeea30c5cdb40f5bcda37782c078c6e) |

### Physics

| Notion page | Local note | Notion ID |
| --- | --- | --- |
| Quantum entanglement | [[quantum-entanglement]] | [53e48b1ea64b4b1bb8f7544a86360e10](https://www.notion.so/53e48b1ea64b4b1bb8f7544a86360e10) |
| Schrödinger equation | [[schrodinger-equation]] | [c6fda5c7e24a495bb0ee82053a5f00bd](https://www.notion.so/c6fda5c7e24a495bb0ee82053a5f00bd) |
| Refraction of light | [[refraction-of-light]] | [04308e74b9a0467d923a5dc3d92acd33](https://www.notion.so/04308e74b9a0467d923a5dc3d92acd33) |
| Doppler effect | [[doppler-effect]] | [3073387111d6466cac2fd69e3cafefbf](https://www.notion.so/3073387111d6466cac2fd69e3cafefbf) |
| Sun | [[sun]] | [5df10e00f1154e8a8429abf2b742530d](https://www.notion.so/5df10e00f1154e8a8429abf2b742530d) |
| Wormholes *(was "Warm Holes")* | [[wormholes]] | [b13f582952de48a2999c53a84df7ade4](https://www.notion.so/b13f582952de48a2999c53a84df7ade4) |
| Chronology protection conjecture | [[chronology-protection-conjecture]] | [5ec5432edb4248ea8c9c2601881ef845](https://www.notion.so/5ec5432edb4248ea8c9c2601881ef845) |

### Indic / astronomy / other

| Notion page | Local note | Notion ID |
| --- | --- | --- |
| Surya Siddhanta | [[surya-siddhanta]] | [f71c8427b1fa40789741c9be05124a63](https://www.notion.so/f71c8427b1fa40789741c9be05124a63) |
| Continent story (geography for Sahasra) | [[continent-story]] | [6400a7bc50da475f85ec0f8f5f852d98](https://www.notion.so/6400a7bc50da475f85ec0f8f5f852d98) |
| Memory palace | [[memory-palace]] | [91f75941bc644574b9a683279193f02e](https://www.notion.so/91f75941bc644574b9a683279193f02e) |

### Professional / interviewing

| Notion page | Local note | Notion ID |
| --- | --- | --- |
| Cisco interviewer training | [[cisco-interviewer-training]] | [82fc9e4dbb5b4cdbb3c4acf6deb532eb](https://www.notion.so/82fc9e4dbb5b4cdbb3c4acf6deb532eb) |

### Security / IoT

| Notion page | Local note | Notion ID |
| --- | --- | --- |
| Resurrecting duckling model | [[resurrecting-duckling-model]] | [8547058e4ebb4446b4468a1367239211](https://www.notion.so/8547058e4ebb4446b4468a1367239211) |
| RFC draft — SZTP CSR | [[rfc-draft-sztp-csr]] | [0586d9ac10eb42f5b4bd2dde208639f5](https://www.notion.so/0586d9ac10eb42f5b4bd2dde208639f5) |

### Meta / note-taking templates

| Notion page | Local note | Notion ID |
| --- | --- | --- |
| Zettle (Knowledge DB) | [[zettle]] | [1ba6eaf11e644336b91033489275d78e](https://www.notion.so/1ba6eaf11e644336b91033489275d78e) |
| Learning Note | [[learning-note-template]] | [74678b4044c546baa77d6fd9382bd8e7](https://www.notion.so/74678b4044c546baa77d6fd9382bd8e7) |
| Reference Note | [[reference-note-template]] | [54d6af69167549569c0cd810881b0d61](https://www.notion.so/54d6af69167549569c0cd810881b0d61) |
| Programming Practice | [[programming-practice-template]] | [173dcddfd66c431baebe9f8f20494b7e](https://www.notion.so/173dcddfd66c431baebe9f8f20494b7e) |
| Subh *(empty precursor to Subhashitani)* | [[subh]] | [7548ca69eac9429fa795e9f108e78231](https://www.notion.so/7548ca69eac9429fa795e9f108e78231) |

## Completion sweep (2026-04-19)

The first migration pass reported "complete" at 39 pages. A follow-up audit enumerating the Notes database directly surfaced **16 additional pages** that were missed — a mix of empty stubs, bookmarks, and a few pages with real content. They were migrated on the same day under the same classification rules (source-bound → literature, concept → research, blank → stub or template).

| Notion page | Local note | Classification | Notion ID |
| --- | --- | --- | --- |
| Hashing | [[hashing]] | research | [161c49b4057e480ea3a99bf1ceb960d5](https://www.notion.so/161c49b4057e480ea3a99bf1ceb960d5) |
| Zettle | [[zettle]] | research (template) | [1ba6eaf11e644336b91033489275d78e](https://www.notion.so/1ba6eaf11e644336b91033489275d78e) |
| Subhashitani | [[subhashitani]] | literature (article) | [1f155991d0574be7888f5898127207fa](https://www.notion.so/1f155991d0574be7888f5898127207fa) |
| Subh | [[subh]] | research (stub) | [7548ca69eac9429fa795e9f108e78231](https://www.notion.so/7548ca69eac9429fa795e9f108e78231) |
| Folding skills | [[folding-skills]] | literature (video) | [e888939c7c184e4e9801826885d01d72](https://www.notion.so/e888939c7c184e4e9801826885d01d72) |
| Sanskrit Dictionaries | [[sanskrit-dictionaries]] | literature (article) | [f77fc21084254751bd7684b44c94634b](https://www.notion.so/f77fc21084254751bd7684b44c94634b) |
| Harmonic Series | [[harmonic-series]] | literature (article) | [e3935f78f50847b395f727f6246d8dad](https://www.notion.so/e3935f78f50847b395f727f6246d8dad) |
| Generating functions | [[generating-functions]] | research | [fd4e71e171844053a106a4f8b3689e20](https://www.notion.so/fd4e71e171844053a106a4f8b3689e20) |
| Generating Functions — Brilliant | [[generating-functions-brilliant]] | literature (article) | [a44a40787bdd4510b0ed664105999744](https://www.notion.so/a44a40787bdd4510b0ed664105999744) |
| Exponents | [[exponents]] | research | [62e380df816349ba8ab1010cf261bdfe](https://www.notion.so/62e380df816349ba8ab1010cf261bdfe) |
| Facebook compression problem | [[facebook-compression-problem]] | research (stub) | [17af27cd697f4edaa3060143f6868ac6](https://www.notion.so/17af27cd697f4edaa3060143f6868ac6) |
| Markdown Diagrams | [[markdown-diagrams]] | literature (article) | [e4997fbd702548bfae279a0c94bcadeb](https://www.notion.so/e4997fbd702548bfae279a0c94bcadeb) |
| Programming Practice | [[programming-practice-template]] | research (template) | [173dcddfd66c431baebe9f8f20494b7e](https://www.notion.so/173dcddfd66c431baebe9f8f20494b7e) |
| Reference Note | [[reference-note-template]] | research (template) | [54d6af69167549569c0cd810881b0d61](https://www.notion.so/54d6af69167549569c0cd810881b0d61) |
| Realtime note detection | [[realtime-note-detection]] | literature (video) | [0eafa0e1ce8742828d6097f50b80eb02](https://www.notion.so/0eafa0e1ce8742828d6097f50b80eb02) |
| Learning Note | [[learning-note-template]] | research (template) | [74678b4044c546baa77d6fd9382bd8e7](https://www.notion.so/74678b4044c546baa77d6fd9382bd8e7) |

## Totals

- **Pilot batch:** 5 pages.
- **First migration wave (post-pilot approval):** 34 additional pages.
- **Completion sweep (2026-04-19):** 16 additional pages (table above).
- **Grand total:** **55** migrated markdown files (plus pre-existing vault files retained in place).

## Open questions / deferred items

- Should published/`Publishable` Knowledge entries get a different tag or path?
- How to handle the `Repeat` / `Retention` spaced-repetition properties in markdown? (Currently dropped.)
- Many Notion pages had "Acquired from Resource" relations to a **Resources** database that was not in this migration scope — the target pages are not yet migrated, so those links remain as raw Notion URLs in body text.
- The Trees Q&A page referenced an attached PDF the migration tool could not extract; [[trees-qa]] is a stub pointing back to [[trees]] and to the original Notion page.
- The Harmonic Series and Generating Functions notes reference PDF attachments (`harmapa.pdf`, `mit-ocw-generating-func.pdf`) that were linked but not inlined — fetch them from the external URL when needed.

## Phase 2 libraries

Phase 2 extended the migration to every remaining database and standalone page in the Notion workspace. Because those databases are dominated by operational ephemera (completed tasks, rolled-over meeting notes, abandoned project hubs) and bookmark-only stubs, the chosen migration pattern was **consolidated library index files** — one per database — with individual literature / research notes written only for content-rich pages. Each library preserves the Notion data-source URI, schema (properties, select options), full enumeration of entries with Notion IDs, cross-references to other libraries, and open threads.

| Database / scope | Notion data source | Local index | Individual notes |
| --- | --- | --- | --- |
| Resources | `collection://...` (Reading DB) | [[reading-library]] | Books, articles, videos under `content/media/{books,articles,videos,podcasts}/` |
| Courses | `collection://...` (Courses DB) | [[courses-library]] | [[mit-6006-introduction-to-algorithms]], [[cisco-golang-course]], etc. under `content/media/courses/` |
| Tutorials | `collection://d7b7aa23-490c-4f4a-a3dd-5680c2235408` | [[tutorials-library]] | [[introduction-to-python]] under `content/operational/tutorials/` |
| Meeting Notes | `collection://db3c620f-ba62-4d5f-8fb6-b2300c4cf36e` | [[meeting-notes-library]] | *(none individually — all ~55 entries indexed)* |
| Projects | `collection://5f844bdf-b690-4309-8550-969c97157406` | [[projects-library]] | *(none individually — ~27 entries indexed)* |
| To-Do | `collection://7a51905f-5721-4a9a-babb-211dfaf11fa9` | [[todo-library]] | *(none individually — ~30 surfaced entries indexed)* |
| Journal | `collection://c7e57818-d637-4428-bf63-4973bed188f0` | [[journal-library]] | *(none individually — ~54 entries indexed)* |
| Standalone pages | *(workspace-level)* | [[standalones-library]] | [[cs-fundamentals-preparation-plan]], [[pipes-and-filters-unix-shell]] |
| **Audit sweep (2026-04-20)** | 6 more DBs + Evernote-imports hub | [[additional-content-library]] | *(indexed — Sanskrit / Home / Travel / System-Design clusters)* |

### Phase 2 totals

- Tutorials: 3 entries (1 individual note, 2 blank stubs indexed)
- Meeting Notes: ~55 entries (all indexed)
- Projects: ~27 entries (all indexed)
- To-Do: ~30 surfaced entries (all indexed)
- Journal: ~54 entries (all indexed)
- Resources / Courses: covered by existing [[reading-library]] / [[courses-library]] — pre-dated Phase 2
- Standalones: ~15 enumerated, 2 individual notes + 1 consolidated index

### Audit sweep (2026-04-20)

A post-Phase-2 audit pass against Notion surfaced substantial content the first searches missed. See [[additional-content-library]] for full enumeration. Summary:

- **6 additional databases:** System Design, Interview prep (nested under [[cs-fundamentals-preparation-plan]]), Recipes, Budget (home-remodel), Wiki (teamspace template), Corporate Travel hub.
- **Evernote-imports hub** (`6d60a7ad74464783a5432b4aa0887a63`) containing 5 pre-Notion nested databases (Python, Image processing, Golang, Udacity deep learning, Personal assistant) — ~2016–2017 technical bookmarks.
- **Sanskrit scholarship cluster** of ~23 pages (Amarakosha chapters 1–3, Niruktam, Sanskrit Literature, Sanskrit Parsing, Maheshvara Sutras, kaTapayaadi scheme, Dhatus list, etc.) — **MIGRATED 2026-04-22** into `content/domains/humanities/sanskrit/` as 17 individual notes plus cluster hub [[sanskrit-scholarship]]. Notion parent hub page renamed to *"Sanskrit Literature - Migration done"*.
- **Home / Kitchen remodel cluster** (~7 pages: Kitchen specs, Sink, Backyard design, Pavers, Budget DB).
- **Hawaii 2021 travel cluster** (~6 pages under Completed Vacations hub).
- **Book pages** outside the Resources DB: Outliers, Atomic Habits, Designing Data-Intensive Applications, Understanding Distributed Systems, Hacking the System Design Interview, Google System Design Secrets.
- **Misc:** ~30 standalone templates / ML-setup / article duplicates / Week 1 learning-plan entries.

Approximate addition to migration scope: **~85 further pages** indexed in [[additional-content-library]].

## Possible follow-up passes

1. Rewrite Notion-internal `notion.so/<id>` body links to wikilinks, now that every target is migrated.
2. Promote anything genuinely atomic/evergreen from the research stubs into `content/domains/` permanent notes (e.g. "Θ is the tight bound; O is the ceiling; Ω is the floor").
3. ~~Extend scope to the **Resources**, **Courses**, **Learning Journal**, and **Meeting Notes** databases, if desired.~~ **Done** — see [Phase 2 libraries](#phase-2-libraries).
4. Delete or archive the original Notion pages once the user has confirmed every migrated note reads correctly in Obsidian / Foam.
5. Promote specific library rows to individual markdown files on demand (e.g. if the Secure-ZTP project becomes a post-mortem, promote it from [[projects-library]] to `content/operational/projects/secure-ztp.md`).
6. Preserve Notion template pages (New Standup, Weekly Sync, Daily Entry, Task, Work Item, Add a new task) under a future `content/templates/` directory — enumerated in the respective library files but not yet migrated as workflow templates.
