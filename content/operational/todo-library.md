---
title: "To-Do Library"
date: 2026-04-19
type: index
category: "library/todo"
tags: [todo, tasks, action-items, ztp, cisco, notion-migration]
status: stable
source: "https://www.notion.so/f8e9df93225e4b5a852e4700003aa3d0"
related: [
  "[[notion-migration]]",
  "[[projects-library]]",
  "[[meeting-notes-library]]",
  "[[journal-library]]",
  "[[reading-library]]",
  "[[courses-library]]",
  "[[tutorials-library]]"
]
---

# To-Do library — Notion To-Do database

Consolidated index of the Notion **To-Do** database (`collection://7a51905f-5721-4a9a-babb-211dfaf11fa9`). The database holds Cisco work items, action items from meetings, personal tasks, and template pages. Most entries are transient — once completed, their content value decays quickly.

## Why a library file

To-Dos are **operational ephemera** — tasks completed or superseded lose their value. The useful residue is in the relations: which To-Do belonged to which Project, which meeting produced it, which reading-list item needed attention. That graph is what this index preserves. Individual task migration would create many one-line markdown files pointing at outdated deadlines.

Same dual-track pattern as [[reading-library]], [[courses-library]], [[meeting-notes-library]], [[projects-library]], [[journal-library]], [[tutorials-library]].

## Database schema

- **Database:** To-Do (`collection://7a51905f-5721-4a9a-babb-211dfaf11fa9`)
- **Properties:** `Name`, `Status`, `Priority`, `Owners`, `Do Date`, `Due Date` (formula), `Effort`, `Impact`, `Estimated hours to complete`, `Done`, `Date Created`, `URL`, plus relations to Projects, Meeting Notes (via Projects), Courses, Tutorials, Reading, and self-relations Parent Task / Subtasks.
- **Status options:** Next Up, In Progress, Completed, Waiting.
- **Priority options:** High 🔥, Medium, Low.
- **Owners options:** Amrit (brown), Akshat (yellow), Naren (blue), Shwetha (blue), Rishi (gray).

## Notable / surfaced entries

These entries were surfaced by keyword searches; the list is **not exhaustive** (Notion search caps at 25 per query, and the DB has relations back-pointing from many Project / Meeting notes).

### ZTP / Secure-ZTP work items

| Title | Notion ID | Likely Project |
| --- | --- | --- |
| Respond to Sundar's (CW) Queries | `26f405d0f59e49bebd8786d192656568` | Secure ZTP |
| By 11 AM: Create work items and estimates for sztp pending items | `0b2e01a0233046a09f5d816c7dc431e3` | Secure ZTP |
| Naren to update the wiki with more details | `be059383aabd4f26aa17db3cea3033a0` | Secure ZTP |
| Naren and Jabir to share the estimated size of code changes | *(relation only)* | Secure ZTP |
| Naren: Split and track the 7.3.1 and 7.4.1 work items in the SmartSheet | *(relation only)* | Secure ZTP |
| Ishwarya: Get L2 EDCS approved | `60c8949360704998be0d9db363ac94a0` | L2 ZTP |
| Rishi: Secure USB ZTP EDCS Complete and approved | `394fffb4059f4aacb3392925a92d336e` | Secure USB |
| Rishi: Encryption support for Secure ZTP. Facebook ask | `af66516861884b7697b5b1e9e5ac83d6` | Secure ZTP |
| Follow-up on the Secure-ZTP flag | `40ca478539d34978a9dfc87b2d7a39db` | Secure ZTP |
| CT changes for Secure-flag disable | `894dbd81751f4279b10296312d329657` | Secure ZTP |
| Consent token support to disable Secure flag for SZTP and Dependencies. III | `e061b2637b5c411c841194c14fc2a5a9` | Secure ZTP |
| Generate Ownership Voucher for Rao | `ccd1481dcb7d478bb0abc6643726759d` | Ownership Voucher |
| Offline OV Generation | `7fb070721bbb4b7683f136379299d36e` | Ownership Voucher |
| Sharing OV plan with Amrit and Akshat | `c474351d80954bf4a49577047c213b37` | Ownership Voucher |
| Secure ZTP Workflow with Crosswork Cloud With Dan Backman | `fe5f1ba62b5c4fe8b061e3b8c7714df5` | Secure ZTP |
| Secure Flag Jun 8 | `2ad03cd4541d4ab3945e567de947276c` | Secure Flag |
| Writeup for Facebook USB boot issue | `fcc23d8ff303429b89f88894639bce68` | FB ZTP USB Upgrade |
| Review PRRQ for SZTP test plan | `ec576fbede6d4edda6df197d9d11453c` | Secure ZTP |
| Update work items in Arun's sheet | `5620a75e21fb4f7285bb7722477e3487` | General |

### Multi-meeting carryover / working items

Several Secure-ZTP PTeam weekly meetings (see [[meeting-notes-library]]) reference carryover action items that roll forward across 3–5 meetings:
- "Jasmine: Validate Secure ZTP Disable on Spitfire and eXR Platforms"
- "Bazil: To update Secure ZTP Smart Sheet for 741 work items status/eTA"
- "Altaf: Create/Update the Scrubber to track Secure-ZTP Device side DDTSes"

These are logically To-Do entries but appear embedded in meeting notes rather than as standalone DB rows.

### Personal / miscellaneous tasks

| Title | Notion ID | Kind |
| --- | --- | --- |
| \[Recurrent\] Complete all revision tasks | `326c4537abe64795bf03c3612aefd6f7` | Recurring |
| One Task: Summary for B4 | `855a6b38233f42519ac93b4762f84174` | Ad-hoc |
| Cancel Kindle unlimited | *(listed)* | Personal |
| Link the CiscoSSL libraries | *(listed)* | Work |
| Pavers | `f33d4d1d3ebf43e99fc87516d1c905c0` | Home |
| Permit | `23eb5e82f55e4a65b9cc9a8397b8a4c6` | Home |
| 200 Vista roma way Heloc | `cfbc78a3b59649e8a97956d376f4d25d` | Home finance |

### Templates / placeholders

| Title | Notion ID |
| --- | --- |
| Task | `f46102f026514864962d7ce4b9e4e2d8` |
| Task (2023) | `0d0b6ea10e8345ef81c745ad40f6f9be` |
| Work Item | `b2d265b2305f429180be3b4ddfada6be` |
| Add a new task | `6d06abcafc37409ead330ebc9c6fa426` |

## Totals

- ZTP / Cisco work items surfaced: ~19
- Personal / home items: ~7
- Templates: 4
- **Total surfaced: ~30** (the actual DB has more — surfaced items are those that contain keywords from the search passes).

## Cross-references

- **[[projects-library]]** — each To-Do's `Projects` relation points at one or more projects in that index. Secure ZTP alone aggregates ~15 To-Dos.
- **[[meeting-notes-library]]** — To-Dos trace back to the meetings that produced them via the separate "Action Items (Meetings)" DB (`collection://758876be-478e-4e89-8cd1-2106a0bf98ba`).
- **[[reading-library]]** — To-Dos with a `Reading` relation aggregate to items in the Reading DB / reading-library entries.
- **[[courses-library]]** — To-Dos with a `Courses` relation cross-link to courses there (e.g. MIT 6.006 follow-ups, Security Green Belt TLS work).
- **[[tutorials-library]]** — relation to the Tutorials DB; no tutorials surfaced an active To-Do in the search pass.

## Open threads

- If any specific To-Do turns into a durable lesson (pattern, checklist, post-mortem), promote it to a permanent note under `content/domains/` rather than leaving it in this index. Candidate: the full Secure-ZTP 7.3.1 / 7.4.1 work-item split could inform a `secure-ztp-release-playbook.md`.
- The Action Items (Meetings) DB (`b2e7b4885f0c4bcba15ae4f9d30a6720`) is a **separate** DB from this one; it may warrant its own `action-items-library.md` if the two DBs diverged. Based on surface examination they overlap heavily — defer until an audit.
- Recurring template pages ("Task", "Work Item", "Add a new task") should be preserved as workflow templates under `content/templates/` when that directory is created — but they are not literature.

---

*Migrated from Notion on 2026-04-19. Original: [To-Do database](https://www.notion.so/f8e9df93225e4b5a852e4700003aa3d0). See [[notion-migration]].*
