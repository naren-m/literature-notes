---
title: "Additional Content Library — Second Audit Sweep"
date: 2026-04-20
type: index
category: "library/additional"
tags: [audit, additional-databases, evernote-imports, sanskrit, home, travel, system-design, notion-migration]
status: stable
source: "Notion workspace — second audit pass"
related: [
  "[[notion-migration]]",
  "[[reading-library]]",
  "[[courses-library]]",
  "[[tutorials-library]]",
  "[[meeting-notes-library]]",
  "[[projects-library]]",
  "[[journal-library]]",
  "[[todo-library]]",
  "[[standalones-library]]"
]
---

# Additional Content library — second audit sweep (2026-04-20)

A second audit pass against Notion surfaced substantial content that the first-pass searches missed — **six more databases** and a long tail of standalone pages spanning home improvement, travel planning, Sanskrit scholarship, book notes, and Evernote import hubs. This library indexes all of it so provenance is preserved before Notion is decommissioned.

## Why a library file

The Phase 1 / Phase 2 migration focused on the documented "second brain" databases (Notes, Knowledge, Resources, Courses, Tutorials, Meeting Notes, Projects, To-Do, Journal) and known standalone pages. But the Notion workspace also contains:

- An **Evernote imports** hub (`6d60a7ad74464783a5432b4aa0887a63`) with 5 nested databases holding pre-Notion content from an Evernote archive.
- Standalone databases that were not reachable from the main area pages (System Design, Recipes, Budget, Wiki, Interview prep).
- A long tail of hobby / home / travel pages (Hawaii Planner, Kitchen-remodel specs, Pavers, Packing lists) that sit in the Home area.
- Book notes (Outliers, Atomic Habits, Designing Data-Intensive Applications, Understanding Distributed Systems) that were created in-page rather than in the Resources DB.
- Sanskrit scholarship pages (Amarakosha chapters 1–3, Niruktam, Sanskrit Literature, Sanskrit Parsing) that sit outside Resources / Knowledge.

The same consolidated-index pattern applies: operational ephemera and bookmark-only pages are indexed here with Notion IDs, and individual notes are written only when the content is substantive and durable.

## Additional databases (6 new — not in Phase 2)

| Database | Notion URL / data source | Nature | Rows (approx) |
| --- | --- | --- | --- |
| **System Design** | `79969be94e7e4ac4949c610cc5f05844` / `collection://5bd01b96-476b-4215-b234-0ddfdfc2462f` | System-design interview prep bookmarks (YouTube talks, Medium articles, ByteByteGo) | ~10 bookmark rows |
| **Interview prep** | `2f3dae5af29644979b53fbdf9443b5ab` / `collection://cbbdff6e-f22d-48f4-9b8e-9f7a20f8c573` | Nested under [[cs-fundamentals-preparation-plan]]. Bookmark collection for coding-interview prep | ~10 rows |
| **Recipes** | `dddd7cbd80314189b037e0cfa419b957` / `collection://aa4e2cd7-f3af-49c2-acf7-b90e96fd2446` | Cooking recipes — Thai curries, Chinese veg, Instant Pot dishes, pastas. Properties: Star Rating, Total Time, Yield, Tags (Dessert/Dinner/Easy/Breakfast/Lunch/Italian/Spicy/Side/Hearty/Light/Ramen/Mexican/Veggie), Link | ~25+ rows |
| **Budget** | `14843d2b96a44888877ed52ee0f5445c` / `collection://6c1dde67-8ab2-412d-9775-510a994eda6e` | **Home-remodel budget** — nested under Home / Projects. Properties: Room (Kitchen/Dining/HalfBath/LivingRoom/Master Bedroom), Budget (number), Quote (number), Priority (High/Medium/Low) | *unknown row count* |
| **Wiki** | `110ce5394b5849899b353a970859a639` / `collection://c128655d-c033-4cf0-bb56-f534fc9d827a` | Notion's default teamspace-wiki template. Properties: Owner, Verification, Tags (Onboarding/Design/Policies/Vision/Company Updates) — probably empty (template scaffolding only) | *likely 0 rows (template)* |
| **Corporate Travel** hub | `c4dd439186064257bc4b354d8c836c18` | Another Notion template page | 0 rows (template) |

### Evernote imports hub — 5 nested databases

The **Evernote imports** parent page (`6d60a7ad74464783a5432b4aa0887a63`, created 2020-06-09) holds pre-Notion technical bookmarks migrated from Evernote. Each of the five inline databases has its own data source:

| Nested DB | Notion URL | Data source | Content |
| --- | --- | --- | --- |
| **Python** | `be5947f0d034402092f3b107cd81c786` | `collection://76479c1c-1995-4636-baac-ba7c72506ce0` | Python bookmarks (real-python articles, note recognition, SGD) |
| **Image processing** | `f1deff0b176e4c71aef4c8fd8e13e888` | `collection://ed1012c9-c07e-4cad-99b3-df7c3ec586ee` | Image-processing bookmarks |
| **Golang** | `36c66bd8451a4f9982cedc27fa532b4a` | `collection://eb54caf4-4844-4596-9b17-67a878597e2b` | Go language bookmarks. Tags: history, grpc, cmd, Install. Referenced entries: Mack notifier, Getting Code Coverage, grpc-on-UCS-Docker, Build Your Own Distributed DB With Go |
| **Udacity deep learning** | `17eda4f536aa48ec944b46c9e7ddfe0e` | `collection://a16f80f6-c4b5-4fd2-997a-d30c865f43f1` | Udacity DLND course notes. Known entry: "Project 4" (language translation, github.com/gmcgibbon/udacity-dlnd-project-4) |
| **Personal assistant** | `a059b42865064144b208e25ad964873b` | `collection://8d9c7aba-498f-4e88-bed9-c280dc28477c` | Personal-assistant / automation notes |

Additional child pages at the Evernote-imports level:
- **Artificial Intelligence** (`9ab78ed4057a463c8238b37ee369769b`) — sub-hub
- **General Linux Notes** (`ea5da14dfb4e44b8a2aff9a689fb916e`) — sub-hub
- **Machine learning setup** (`817297e82bae4e428c14fd2e7270b8bc`, 2016-07-11) — apt-get build commands for an ML rig

These are technical bookmark archives from ~2016–2017 (pre-dating the main Notes DB). They are not literature-note candidates individually; preserving the index here is sufficient.

## System Design database — bookmark rows (sample)

Entries in the System Design DB and the related standalone system-design-page cluster:

| Title | Notion ID | Kind |
| --- | --- | --- |
| Top 50 System Design Interview Questions for 2024 | `c4507e59663e41d59f524ed6c43e610a` | Article bookmark |
| Design a Chat Application like WhatsApp | `13cbc7a0d8dc81afbf47c87f68f11a32` | Article bookmark |
| Hacking the System Design Interview (Chiang book) | `1b27cd04e9ca496899fcb1dc4ffda8e3` | Book bookmark |
| Google System Design Secrets | `1cd1a3269e30492aa72e7902f03178f0` | Book/article bookmark |
| FAANG Design Yelp (ByteByteGo) | `5ce268d1c4c44b2fbd3e39b1c06c45ea` | YouTube |
| TikTok architecture (sudoCODE) | `ab6b3535001f4edca7a46d3bfa139e42` | YouTube |
| How to design Google Docs (Episode 4) | `05c2b266e3ca4faf906372196ecb324d` | YouTube |
| donnemartin/system-design-primer | `d5434fe388b443d18d3f55a91751a194` | GitHub bookmark |
| A Guide to Consistent Hashing (Toptal) | `0895ff88a33644e4ac8cc62ec557c8ed` | Article |
| High Scalability | `cffa9bea480a4c0cb84e7618f376e418` | Article |
| How to Become a Backend Developer | `d6b8682333e34cca9e0a7587d82f1f88` | Article |
| Amazon coding interview guide (IGotAnOffer) | `5766968a238c4f4db8d13ed1a4e751ec` | Article |
| 500 DSA interview questions (Techie Delight) | `f4ed7835d7cc49e78cdb725f223055f5` | Article |
| Facebook E5 / Google L5 / MS AS 2 offers (LeetCode Discuss) | `5f0cf75156784287b577eadb02bdbaf3` | Article |
| Distributed Systems in One Lesson (Tim Berglund) | `de294886fd2448b78043f7b1e63fc60f` | YouTube |
| Four Distributed Systems Patterns (Tim Berglund) | `63c66a6b531d4f9fa0f68ca8c36e4357` | YouTube |
| Distributed systems (page) | `b99b2e1006b642dda8c130af7e98ee61` | Article / notes |
| Introduction to PostgreSQL physical storage | `c853fcc01a99463caef47458033870d9` | Article |
| Understanding Distributed Systems (Vitillo book) | `bb61097f08904fa0b9ea962e8a7030c6` | Book |
| Designing Data-Intensive Applications (Kleppmann) | `b03df36d9e884808b7926396a097b24a` | Book |

The system-design bookmark cluster is the Notion-side companion to [[cs-fundamentals-preparation-plan]]. For durable study reference, [[teach-yourself-computer-science]] + Kleppmann is canonical.

## Book notes — standalone book pages (not in Resources DB)

| Title | Notion ID | Kind |
| --- | --- | --- |
| Outliers (Gladwell) | `acd960943d164bcba61155a34631a2fb` | Book notes — "mathematical ability" + IBM Joy / rewriting UNIX excerpts |
| Atomic Habits (Clear) | `3da81ca352de4b429784326284fcf7a1` | Book notes |
| Designing Data-Intensive Applications (Kleppmann) | `b03df36d9e884808b7926396a097b24a` | Book product page |
| Understanding Distributed Systems (Vitillo) | `bb61097f08904fa0b9ea962e8a7030c6` | Book product page |
| Hacking the System Design Interview (Chiang) | `1b27cd04e9ca496899fcb1dc4ffda8e3` | Book product page |
| Google System Design Secrets | `1cd1a3269e30492aa72e7902f03178f0` | Book product page |

If any of these develops into substantive reading notes, promote to `content/media/books/<slug>.md`. The product-page entries (Amazon paste-ups) can stay as rows — they carry no reading-notes content.

## Sanskrit scholarship cluster

Pages outside the Knowledge / Resources DBs that form a coherent Sanskrit / Indic-studies thread:

| Title | Notion ID | Kind |
| --- | --- | --- |
| Amara Kosham (hub) | `c51dd62d13da41aeacb986812a244f5c` | Hub page |
| Amarakosha or Namalinganushasanam, Thesaurus Chapter 1 | `824e1e3c28a145fba54d4881e0ebe4a0` | Sanskrit text |
| Amarakosha Thesaurus Chapter 2 | `3acd1ff9935546a086b1627e3d928876` | Sanskrit text |
| Amarakosha Thesaurus Chapter 3 | `be5e178190d84d3bb7dab923badaa464` | Sanskrit text |
| Amarakosha Words Devnagari Glossary (Google Drive) | `a1dc49b55f3848fdb5d913d375e971e7` | PDF bookmark |
| amarkosh_english.pdf | `93a86966a742438cbb668d15b7acb372` | PDF bookmark |
| Amara Kosha Audio (Internet Archive) | `a34902c4b3344bc6baee25a4e5c8feb8` | Audio bookmark |
| Session 01 — Learn to chant Amarakosha (YouTube) | `17c4702d929c404cb7f77702b7a4f9cc` | Video |
| amarakosha : Sanskrit Documents | `af2a7560953d459eac5707ccce018360` | Source corpus |
| Raw amara_pada.csv (GitHub raw) | `b7a7b80426c34746a72ed231710707d0` | Data file bookmark |
| Raw amara_pada.csv (duplicate) | `84560fdf518c493caaa00cd0e31225b0` | Data file bookmark |
| Niruktam | `143e387c144c4ca4835c3a1e24af76d1` | Scholarship page |
| Sanskrit Literature | `bbedb1ae481a49de9ec7fdeda525fa79` | Hub page (references sanskrit/chandas meter-recognizer) |
| Sanskrit Parsing | `0a6a837f53b643b087f2e42fbb61d5f1` | Research thread |
| The Complete List of Dhatus (HitXP) | `d8cab5b0e49e4815bbdf5a8d771fc482` | Article |
| Maheshvara Sutras (Matheson Trust) | `9b636296a46e4653b3698119dfbcbf8b` | Article |
| Planetary Linguistics | `cce5ae8c182e440d8d4906d2d8f3c549` | Article |
| Health Verses in Sanskrit (Ayurveda habits) | `7ec1daef83dc42f8954731877f30a82a` | Article |
| Kanakadhara Stotram (YouTube) | `b741db8b8253401ebdf8dd1c3a853169` | Video |
| Mahishasura Mardini — Aigiri Nandini | `f64c82a66e0248d78465a04b2e563c95` | Article |
| Sree Mahishaasura Mardini Stotram (Telugu meaning) | `85282d82aaa04084b425f3a014067d78` | Article |
| The "kaTapayaadi" scheme applied to Melakarta Ragas | `c11f50763bdf466e917a56418c28d025` | Article (music theory) |
| India | `5d1d2e8e6dcc41a39fe756d587ce433d` | Hub / notes page |

**Status (2026-04-22): MIGRATED.** The full Sanskrit cluster has been migrated into `content/domains/humanities/sanskrit/` as 17 individual markdown files (amara-kosham-hub, amarakosha-chapter-1/2/3, niruktam, maheshvara-sutras, mahishasura-mardini-stotram, mahishasura-mardini-telugu, kanakadhara-stotram, sanskrit-dhatus, sanskrit-chandas-meters, katapayadi-scheme, planetary-linguistics, ayurveda-health-verses, india-max-muller-highlights, sanskrit-parsing) plus the cluster hub note **[[sanskrit-scholarship]]**. The Notion parent hub page has been renamed to *"Sanskrit Literature - Migration done"* to signal completion. This table now serves as a provenance index pointing from Notion IDs to the migrated vault notes.

## Home / Kitchen remodel cluster

Pages under the Home area — kitchen remodel, paver / backyard, sinks, budget planning:

| Title | Notion ID | Kind |
| --- | --- | --- |
| Home (area hub) | `9fe8fdbf7410432c9771e6a844f031a6` | Area hub |
| Kitchen (2022 version) | `dc03d4797a5948d2bd64f4207842d708` | Remodel spec |
| Kitchen (2023 version) | `4614568ca62644f9afac4eac23eed967` | Remodel spec |
| Sink | `ed517b2cb50443e1a869c47828c497a7` | Product spec |
| Draw out for Under kitchen sink | `12b6d242b62e480ab85ac0f771316088` | Organization ideas |
| Backyard and frontyard design ideas | `dd57b4ac67914191a5d51ddaeeb93b9a` | Remodel spec |
| Pavers | `f33d4d1d3ebf43e99fc87516d1c905c0` | Purchase-prep notes (also in [[todo-library]]) |

These are operational / home-improvement records; rolling them into the Home project under [[projects-library]] is the right move rather than promoting individually.

## Travel cluster — Hawaii 2021

Pages under a "Completed Vacations" hub around the July 2021 Hawaii trip:

| Title | Notion ID | Kind |
| --- | --- | --- |
| Completed Vacations (hub) | `b81dca4531464294a22b46e60e86e764` | Hub |
| Hawaii Planner | `e640adc3ba2d42f29358175754672e03` | Trip plan |
| Pre Travel Actions | `0fb3836bc6ec4504a07803546b6149d0` | Checklist |
| Packing Listening (packing list, 2021) | `87d902e1bddb4a5aa0cd505c2572768b` | Checklist |
| Laniakea Beach | `ba66be062f6b44b1b0e95ad5767454ac` | Destination notes |
| Return Flight | `ed51e7f7713147b7950f556b463cfd4b` | Itinerary |

Operational / personal records — indexed here rather than individually migrated. If a future trip planner wants to pattern-match off Hawaii 2021, the Notion page is the source.

## Misc standalone pages surfaced

| Title | Notion ID | Kind |
| --- | --- | --- |
| Teamspace Home | `3b302978ce2e4adb87d2fb3ecb79aa93` | Notion template hub |
| Getting started with meeting notes | `6779922c2b014f648633d33d0def3a38` | Template |
| Getting started with docs | `98f808b8610b4b768034a433192326d3` | Template |
| Getting Started | `7e6f93b626964c13b15c7169eafadc49` | Template |
| New Page With Tags | `3398379fd5f347dc9cf5a5bceb83384c` | Template |
| Facebook (2017 ad-hoc) | `079f8b4afdcb4879845a963fa5db0710` | Resume / recruiter note |
| Installing grpc on UCS/Docker | `0a1cc7ae027241c5bf728f3d7a7c84e8` | Tech notes (2017) |
| Mack notifier | `0265a6244bfe4296814d8c6de20df153` | Golang tool notes (2017) |
| Getting Code Coverage from External Testing | `334c8264b4a74e318d99e75507e3810e` | Article bookmark |
| PythonInMusic | `95fe646026494635b031e88d8a2d4d22` | Article bookmark |
| Knowledge Processing System (Tinderbox) | `85482aaf07004dc7920393c078441e18` + `c57abd2bd0354720a95e38d50e7a350d` | Article (2 copies) |
| Entire Computer Science Curriculum in 1000 YT Videos | `ddd6e60451134b358e1a714c27b53052` | Article |
| Advanced Topics in Operating Systems (Stanford) | `278f248bd2bf458687f29994fa49329e` | Course bookmark |
| Introduction to Operating Systems | `4af0b943cba74e8583f8f0f286de03a9` | Course bookmark |
| MIT courses | `4cfe75f1becd4caa9edfd6d95ae962bb` | Course list bookmark |
| Week 1 (× 4 duplicates from 2020 learning plan) | `e7c73affbd6347e191cfba6883d5c5cd`, `1c1fe718d8fe4d109b3c9354d5a04f85`, `08e59e73c0fc46fba84d952dade18eb0`, `8b9d1b27664848198fe13f601e363696` | Learning-journal entries |
| Monday: Plan and design | `bb975c3f7fcf4890b56c53b7f6660c27` | Planning entry |
| Interview Training | `3e14d8dd1e394d86b15ebb4485e6030c` | Page |
| Why Are Some Programming Languages Faster Than Others? | `00119072da9b4b98ac9f4cae67e3ee2a` | Article |
| Note Recognition In Python (Medium) | `b2258c90eed84bd89d08ccdbad0dc1e0` + `23d255af4bb843e4896d5eb83bdff1f7` + `b491d82d8da54d2b948396f6e90f533c` | Article (3 duplicates) |
| Stochastic Gradient Descent with Python and NumPy | `582f36238a8d4a47831551c4a634b8e9` | Article |
| k-Nearest Neighbors (Real Python) | `ae3fb2b6ae4b46a28c6a022198050046` | Article |
| Machine Learning Is Fun! Part 4 | `a504e0f3c2404168b2b94d4aabe124b6` | Article (duplicate of the existing literature note) |
| Deep Learning Raga Classification (Carnatic) | `0828d3e55604419faf27d1beea9a7ff5` | Article |
| Ashtanga Hrudayam (alternate copy) | `9c8462bb2edc4981ad44298c56357fa6` | Book notes (alternate to existing [[AshtangaHrydayam]]) |
| Project 4 (Udacity DLND) | `f69bcc12c1194b67988691d75498b82a` | Project notes |
| Feb 11, 2022 (daily entry) | `5c2b4a72c54a4eac9faa5fbac50cd19c` | Journal-adjacent |

## Totals — second audit sweep

- **Additional databases:** 6 (System Design, Interview prep, Recipes, Budget, Wiki, Corporate Travel hub)
- **Evernote-imports nested DBs:** 5 (Python, Image processing, Golang, Udacity DL, Personal assistant)
- **Book notes / reading pages:** ~6
- **Sanskrit cluster:** ~23 pages
- **Home / Kitchen cluster:** ~7 pages
- **Travel cluster:** ~6 pages
- **Misc standalones / templates / duplicates:** ~30 pages

**Approximate addition to migration scope: ~85 further pages** on top of the Phase 1 (55) + Phase 2 (~170) counts.

## Cross-references

- **[[notion-migration]]** — master migration hub (now updated to reference this audit).
- **[[projects-library]]** — "Home" project should ideally own the kitchen-remodel cluster; "Sahasra" / "Personal" projects cover others.
- **[[cs-fundamentals-preparation-plan]]** — parent of the Interview prep nested DB.
- **[[teach-yourself-computer-science]]** — canonical replacement for the ad-hoc system-design and backend-learning bookmarks.
- **[[todo-library]]** — "Pavers" and home-finance items appear there too.
- **[[reading-library]]** — books in this index should fold into reading-library's book section; they're duplicates because they were added as standalone pages rather than Resource rows.

## Open threads

- **Evernote imports cluster** is pre-2017 and unlikely to be revisited. If the Notion workspace is deprovisioned, archive this whole branch to a zip rather than migrate individual entries.
- **Sanskrit cluster** is the strongest candidate for a permanent note: `content/domains/humanities/sanskrit-scholarship.md` could aggregate the Amarakosha chapters, Niruktam, Maheshvara Sutras, kaTapayaadi scheme into one coherent research hub. This is the "durable lesson" hiding in the standalone pile.
- **Recipes database** is genuinely useful — consider exporting to CSV from Notion before deprovisioning, or capturing the top-rated recipes as a `content/operational/recipes.md` list.
- **Home Kitchen remodel** — the Budget DB carries real numbers. Export to CSV before deprovisioning if the numbers still matter, or roll into a private financial records store.
- **Hawaii Planner** could become a reusable trip-planning template at `content/templates/trip-planner.md` when templates directory is created.
- **Duplicates** (Note Recognition × 3, Knowledge Processing × 2, amara_pada.csv × 2, Machine Learning Is Fun! Part 4 alternate) are Notion-UI artefacts — safe to ignore.
- **Wiki database** is almost certainly the empty Notion teamspace-wiki template. Confirm at deprovisioning time.

---

*Migrated from Notion on 2026-04-20. Second audit pass — see [[notion-migration]] for full workspace map.*
