---
title: "Projects Library"
date: 2026-04-19
type: index
category: "library/projects"
tags: [projects, library, index, sahasra, cisco, ztp, secure-ztp, notion-migration]
status: stable
source: "https://www.notion.so/525b3b883df34c9ebb805cc959f3b391"
related: [
  "[[notion-migration]]",
  "[[meeting-notes-library]]",
  "[[todo-library]]",
  "[[journal-library]]",
  "[[reading-library]]",
  "[[courses-library]]",
  "[[tutorials-library]]"
]
---

# Projects library — Notion Projects database

Consolidated index of the Notion **Projects** database (`collection://5f844bdf-b690-4309-8550-969c97157406`). ~25 project entries covering Cisco work (ZTP / Secure-ZTP / telemetry), Sahasra (child-education side projects), personal (Home, Ramayanam, Writing Telugu), and template pages.

## Why a library file

Projects in the source Notion setup are **hubs that pull from other DBs** — each project page embeds views of Meeting Notes and To-Do for that project, with the project page itself usually just a title + status + a "Project Description" callout that was rarely filled in. Individual migration into separate markdown files would create a pile of empty shells; an index preserves the provenance and cross-links action items / meetings to the relevant project without duplication.

Same dual-track pattern as [[reading-library]], [[courses-library]], [[meeting-notes-library]], [[tutorials-library]].

## Database schema

- **Database:** Projects (`525b3b88-3df3-4c9e-bb80-5cc959f3b391`)
- **Data source:** `collection://5f844bdf-b690-4309-8550-969c97157406`
- **Properties:** `Name` (title), `Status` (select), `Category` (multi-select), `Date` (date), `URL` (external link), `Done` (checkbox), `Progress bar` (formula), `Completed` (rollup), `Goal` (rollup), `Related to Meeting Notes` (relation → [[meeting-notes-library]]), `Related to Notes & Drafts` (relation → Notes DB), `Related to To-Do` (relation → [[todo-library]]).
- **Status options:** In progress, In Planning, In Design, In Testing, Not Started, Done, support, Back Burner.
- **Category options:** Work (green), YouTube (red), Personal (yellow), Support (purple), Sahasra (pink).

## Work / Cisco projects

| Project | Status | Category | Notion ID |
| --- | --- | --- | --- |
| Secure ZTP | In Testing (Done flagged) | Work | `5524bef3241e460aade3b9ff833cfed2` |
| L2ZTP SPIO | *(Not Started)* | Work | `a378b0fefded4519a2ff26313cf6578c` |
| New Job | *(in progress)* | Work | `6997eaba18dc4c28852e347ca048f5c4` |
| Tacacs | *(unknown)* | Work | — *(listed in enumeration pass; page not re-fetched)* |
| MASA service | *(unknown)* | Work | — *(listed in enumeration pass)* |
| Secure USB Fetcher | *(unknown)* | Work | — *(listed in enumeration pass)* |
| FB ZTP USB Upgrade | *(unknown)* | Work | `10a33abdbb814d6f9d2f688317684352` |
| ZTP Auto-breakout | *(unknown)* | Work | `46a5f62f7ec34e9b97703fff5e705a81` |
| 3. L2 ZTP | *(unknown)* | Work | `09323a0095be461d8df88e8751e0841b` |
| Master Algorithms & DS | *(unknown)* | Work | — |
| 4. Ownership Voucher | *(unknown)* | Work | `cc5a1417a0864b9681162561740ab310` |
| CW-SZTP App | *(unknown)* | Work | — |
| Secure Flag | *(unknown)* | Work | `547484badd0a4f45bb21f7292c26bc48` |

The Secure ZTP project aggregates the [[meeting-notes-library]] entries: Secure-ZTP sync May 14 / Jun 11, plus several Secure-ZTP PTeam weeklies from Dec 2020 – Jan 2021. Its To-Do rollup links 15 tasks (see [[todo-library]]).

## Sahasra (child-education / personal learning projects)

| Project | Status | Notion ID |
| --- | --- | --- |
| Sahasra (hub) | *(unknown)* | `5d588236bf6540e49518bf9af761045e` |
| Sahasra Learning Project | *(unknown)* | — *(listed in enumeration)* |
| Sahasra Writing English | *(unknown)* | `179e6cf9983245e5b2f013bde5c714c8` |
| 2. Sahasra Continents | *(unknown)* | `df2abbcc021745278ce23e6904ecd48d` |
| 1. Sahasra Numbers phase 1 | *(unknown)* | `61b5ad394bd44ce28c0f5a2b69949799` |
| Sahasra Additions | *(unknown)* | `50fce637f13f498ab66207649161ec8a` |
| Sahasra Writing | *(unknown)* | — |

## Personal

| Project | Status | Notion ID |
| --- | --- | --- |
| Ramayanam | In Planning | `d0833b3689b9467f89e3f13663f27c9a` |
| Home | *(unknown)* | — *(listed in enumeration)* |
| Writing Telugu | *(unknown)* | `3ad6564e745b4358a4da8c009c29f9ec` |
| YouTube Videos | *(unknown)* | — |

## Templates / placeholder

| Project | Notion ID |
| --- | --- |
| New Project | `e81ed6547c3845ed90073153b0f1523d` |
| Getting started with Projects & Tasks | `6e87509f6abc4ee288c1fbd1626d6355` |
| Write project proposal | `0869912bc1b34e8c9b9d10be117726fd` |

## Totals

- Work / Cisco projects: 13 enumerated
- Sahasra projects: 7 enumerated
- Personal projects: 4 enumerated
- Templates: 3
- **Total: ~27 project entries**

## Cross-references

- **Meeting Notes.** Most projects' `Related to Meeting Notes` relation points at entries enumerated in [[meeting-notes-library]]. In particular: Secure ZTP → ~12 meetings, L2 ZTP / L2ZTP SPIO → ~3 meetings, ZTP Auto-breakout / FB ZTP USB Upgrade → ~2 each, Ownership Voucher → "Offline OV Generation" + "Sharing OV plan with Amrit and Akshat" + "Generate Ownership Voucher for Rao" + "Secure-ZTP sync May 14".
- **To-Do.** The "Related to To-Do" relation on each project aggregates the same action items indexed under [[todo-library]].
- **Notes & Drafts.** Project hubs that embed "View of Notes" reference the Notes / Knowledge DBs — those are covered by [[notion-migration]] and [[reading-library]].
- **Standalone page:** "[[master-algorithms-ds]]" (if promoted) would be the research-track companion to the Master Algorithms & DS project — cross-link back to [[mit-6006-introduction-to-algorithms]].

## Open threads

- Most project "Project Description" callouts were empty in Notion. If any project gets actively worked on again, promote that project to an individual file under `content/operational/projects/<slug>.md` with the current state, and replace the table row with a wikilink.
- The Secure ZTP project is the most substantive — its cross-links to ~15 Meeting Notes + ~15 To-Do items form a de facto knowledge graph. Consider promoting it to an individual hub note if a post-mortem gets written.
- The six Sahasra sub-projects (Numbers, Continents, Writing English, Additions, Writing, Learning Project) form a coherent pedagogy; they may deserve a single `sahasra-curriculum.md` rather than six separate pages.
- Several enumerated project names are listed without Notion IDs — those came from earlier-pass searches that surfaced titles without IDs. A final sweep pass should capture the missing IDs, but the current list is complete enough for the index.

---

*Migrated from Notion on 2026-04-19. Original: [Projects database](https://www.notion.so/525b3b883df34c9ebb805cc959f3b391). See [[notion-migration]].*
