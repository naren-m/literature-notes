---
title: "Meeting Notes Library"
date: 2026-04-19
type: index
category: "library/meeting-notes"
tags: [meeting-notes, cisco, ztp, secure-ztp, gnmi, standup, weekly-sync, notion-migration]
status: stable
source: "https://www.notion.so/e4b040ec6d614688b5baa4e4582ea709"
related: [
  "[[notion-migration]]",
  "[[projects-library]]",
  "[[journal-library]]",
  "[[reading-library]]",
  "[[courses-library]]",
  "[[tutorials-library]]"
]
---

# Meeting Notes library — Notion Meeting Notes database

Consolidated index of the Notion **Meeting Notes** database (`collection://db3c620f-ba62-4d5f-8fb6-b2300c4cf36e`). The database tracks ~35 distinct meeting entries from 2020–2023, dominated by Cisco Secure-ZTP / ZTP feature work with later additions around gNMI / gNOI / gNXI auth.

## Why a library file

Meeting notes are **high-volume, low-individual-value** artefacts. Each one was a point-in-time set of action items, most of which have since been closed, superseded, or rolled into permanent project pages like [[secure-ztp]] / [[l2-ztp-spio]]. Rather than migrate each one into its own markdown file, this index preserves the provenance and lets specific meetings be promoted to standalone notes only if they turn out to matter (e.g. a post-mortem that contains durable lessons).

Same dual-track pattern as [[reading-library]], [[courses-library]], [[tutorials-library]].

## Database schema

- **Database:** Meeting Notes (`e4b040ec-6d61-4688-b5ba-a4e4582ea709`)
- **Data source:** `collection://db3c620f-ba62-4d5f-8fb6-b2300c4cf36e`
- **Properties:** `Name` (title), `Meeting Date` (date), `Participants` (person), `Project` (relation → Projects DB), `Type` (select), `Related to Action Items (Meetings)` (relation → Actions DB), plus auto Created / Last Edited.
- **Type options:** Post-mortem (red), Standup (green), Weekly Sync (blue), Sprint Planning (yellow), Ad Hoc (orange), ztp (pink), Feature (brown), ztp_dependency (gray).

## DE-DT Sync series (recurring Cisco Design-Engineering ↔ DT sync)

| Date | Title | Notion ID |
| --- | --- | --- |
| 2021-03-18 | Mar 18: Dev-DT Sync | `a771ace8b48b471fa2f57730c70edd4d` |
| 2021-03-25 | Mar 25: Dev-DT Sync | `20273c29885c42029b8c8384b02148ba` |
| 2021-04-01 | Apr 1: Dev-DT Sync | `fac3fb27d9d14f31a813e90b510637f3` |
| 2021-04-22 | Apr 22: Dev-DT Sync | `80ad4325b7554d9bb4ce047cab7a7151` |
| 2021-04-29 | DE-DT Sync Apr 29 | `aa73b6caaf1348e688e01f77be67f55d` |
| 2021-05-11 | DE-DT Sync May 11 | `cbaf647e2328440688eb1be718ff3210` |
| 2021-05-20 | DE-DT Sync May 20 | `47ecc1ead0de4522bc3bb3e762f9bf56` |
| 2021-05-27 | DE-DT Sync May 27 | `1f000ec6d0344f2e83e0f2c2ade441ff` |
| 2021-06-03 | DE-DT Sync Jun 3 | `43b44f16d63a4e18ad94edcdbad3f39f` |
| 2021-06-10 | DE-DT Sync Jun 10 | `a68bfe2b5c654573a10c3c273870eb16` |
| 2021-06-16 | DE-DT Sync Jun 16 | `2a68cd7389d645f3a69a57b2be3aae3e` |
| 2021-06-24 | DE-DT Sync Jun 24 | `d9d6f79a45e647c48740f4eb1381eea7` |

Recurring theme: "Barsha to update the DT sync wiki with TIMs link for Secure ZTP USB." Twelve instances span Mar–Jun 2021.

## Secure ZTP PTeam weekly / program syncs

| Date | Title | Notion ID |
| --- | --- | --- |
| 2020-06-10 | Secure-ZTP sync May 14 | `bf759c130e214de08ce1c2751d1d501c` |
| 2020-06-12 | Secure-ztp sync Jun 11 | `a54175bed3024d9ea07e8b9b62009a0c` |
| 2020-11-25 | Secure ZTP sync. Nov 25 | `c6800dae01394c0a8e5cca6599aead8b` |
| 2020-12-08 | Dec 8: Secure ZTP PTeam weekly | `d33e481f8be44ff58c32062983a95e00` |
| 2020-12-15 | Dec 15: Secure ZTP PTeam weekly | `446927e444264a5789d4ddc9d3cbfe63` |
| 2021-01-05 | Jan 5: Secure ZTP PTeam Weekly | `1b9ab4ba1619435db5e244d48d97941b` |
| 2021-01-12 | Jan 12: Secure ZTP PTeam Weakly | `63c57131e70a43c2a8f2fc549042676a` |
| 2021-01-19 | Jan 19 Secure ZTP PTeam Weakly | `c616c80651e441f995874c13c0eb8823` |

Recurring theme: CW demo feedback, scrubber DDTS tracking, 7.3.1 Secure ZTP rollout, TAM / Hybrid TAM platform coverage (ASR9K).

## ZTP feature & architecture ad-hoc meetings

| Date | Title | Type | Notion ID |
| --- | --- | --- | --- |
| 2020-06-02 | Secure ZTP Flag | Feature | `18dbc3aa5546473680f2a4221b558678` |
| 2020-06-02 | Secure ZTP Flag May 28 | ztp | `23b9cbfdb15f495898cb9dc82443e147` |
| 2020-06-23 | Microsoft Escalation on disabling ZTP | Ad Hoc | `6a39b3a3f9834816ad795e0979019acc` |
| 2020-10-12 | Secure ZTP disable with Consent Token commit plan for 7.3.1 | Feature | `631247bfca1e4737aab9a38539981528` |
| 2020-10-20 | CT app changes for ZTP | Feature | `7cfbc2bd4f3e4c238595a2b53add0ab8` |
| 2020-10-30 | Legacy ZTP lackings Security workflows | Ad Hoc | `7dd8ae1646d04ea0a7b040dfe0d502a7` |
| 2020-11-23 | Suresh: Legacy ZTP ASIG | Ad Hoc | `a2c301577ddc4bc7a17f808ef155aed8` |
| 2020-12-11 | Secure ZTP with USB | ztp | `33059f13b24c45c9ba0e889e489c9448` |
| 2021-01-21 | ASIG/XR Architecture. Legacy ZTP Security | Ad Hoc | `d11faa4044db41d0bd89b429085df1c0` |
| 2021-03-11 | ZTP TTS | Ad Hoc | `da8472416fb24495b8f0c427329be63c` |
| 2021-03-12 | ZTP CLI | Feature | `3dccc1fe107841879d9c48f1fce47d70` |
| 2021-04-28 | Dish config Meeting | Ad Hoc | `4d012aeb9ac94c37b8276012d5a95f65` |
| 2021-06-14 | 3. L2 ZTP | Feature | `09323a0095be461d8df88e8751e0841b` |
| 2022-03-01 | ZTP Auto-breakout | Feature | `46a5f62f7ec34e9b97703fff5e705a81` |
| 2022-03-01 | FB ZTP USB Upgrade | Feature | `10a33abdbb814d6f9d2f688317684352` |

## gNMI / gNOI / gNXI (later program focus)

| Date | Title | Notion ID |
| --- | --- | --- |
| 2022-03-10 | gNMI Path Level Auth | `cd0359d6dc0e47aa958a356f1221492b` |
| 2022-03-10 | OC Auth: Schedule meeting with YFW, NACM for gNMI scoping | `547c313f4f694de1bb32c38cbfe047ac` |
| 2022-03-28 | gNXI Readout | `aee4672edcad4e789678ab6470781acd` |
| 2022-07-25 | gNOI Ping | `7bcfc756b27c456eb140545c9ddb4e11` |
| 2022-12-22 | Weekly Update | `37aaa88db9a84ba088f7256cdc790231` |

## Misc standups, reviews, and templates

| Date | Title | Kind | Notion ID |
| --- | --- | --- | --- |
| 2020-05-08 | Weekly Sync | Template | `b9309843f4c24fceb4a059b92318cb62` |
| 2020-05-08 | Sprint Planning | Template | `35a76cb3ab604fb9ad28ee36cec84b77` |
| 2020-06-27 | Jun 26 | Journal-like | `15a2c40e82dd4ab78937009f5bbe6a77` |
| 2020-08-12 | Setup meeting with Amrit | Ad Hoc | `8dce23216e324efeb98fbd9d48ca10f3` |
| 2020-09-04 | Review PRRQ for SZTP test plan | Review | `ec576fbede6d4edda6df197d9d11453c` |
| 2021-01-08 | Review @Not found | Review | `d7a48db351854c0191fdece8f099595b` |
| 2021-05-21 | Review on TeamsWeek | Review | `5ca490a8d9e34d1daa3f62caa51df288` |
| 2021-07-18 | Review Qip | Review | `770d7486d5904955b37401ef133d3079` |
| 2021-11-05 | Yearly Review | Review | `69b785eaf55e4f8aaf6044cbd4833435` |
| 2022-02-25 | Copy collected data into the sprint document | Task-like | `72214c257a2c4c9991da053044106c12` |
| 2023-07-31 | Team Standup @July 31, 2023 | Standup | `84eba11570b34cd29a20440bc354cfc0` |
| 2023-07-31 | New Standup | Template | `e2c61b5c3db0431f98646581c5192744` |
| 2023-07-31 | Review research results | Template | `c75f3c77da6243f0a42a6ae01af3a7b1` |
| 2023-07-31 | Schedule kick-off meeting | Template | `97bca8e146724a63940efcfc9d65da38` |
| 2023-07-31 | Getting started with meeting notes | Template | `6779922c2b014f648633d33d0def3a38` |

## Totals

- DE-DT Sync series: 12
- Secure ZTP PTeam weeklies: 8
- ZTP feature / architecture ad-hocs: 15
- gNMI / gNOI / gNXI: 5
- Misc standups, reviews, templates: 15

**Total: ~55 meeting entries** (count is approximate — Notion search is capped at 25 per page; five overlapping searches were unioned).

## Cross-references

- Most of these meetings attach to the [[secure-ztp]], [[l2-ztp-spio]], [[ztp-auto-breakout]], [[fb-ztp-usb-upgrade]], [[secure-usb-fetcher]], [[tacacs]], [[ownership-voucher]] projects — see [[projects-library]] for the project index.
- Action items from these meetings are tracked in a separate Notion DB (`collection://758876be-478e-4e89-8cd1-2106a0bf98ba` — "Related to Action Items (Meetings)"), most of which now live in [[todo-library]].
- Post-mortem types, if any, are candidates for promotion to permanent notes under `content/domains/` — durable lessons survive the meeting record.

## Open threads

- If any specific meeting turns out to be cited from another note, promote it to an individual file under `content/operational/meetings/<date-slug>.md` and replace the row here with a wikilink. Candidates: the two Secure-ZTP syncs that pre-date the Jun-2020 migrations, and the Jan-2021 ASIG architecture call.
- The "Getting started with meeting notes", "New Standup", "Weekly Sync" template pages should be preserved as workflow templates under `content/templates/` when that directory is created — but they are not literature.
- The Jun 26 page is more of a journal entry than a meeting; cross-link it from [[journal-library]] too.

---

*Migrated from Notion on 2026-04-19. Original: [Meeting Notes database](https://www.notion.so/e4b040ec6d614688b5baa4e4582ea709). See [[notion-migration]].*
