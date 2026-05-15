---
title: "Reading Library — Resources DB Index"
date: 2026-04-19
type: research
category: "meta/migration"
tags: [migration, notion, reading-list, index, resources]
status: in-progress
source: "Notion workspace (Resources DB, collection://87f22aa2-52ac-4f05-8cd4-3f67e5a4901b)"
related: ["[[notion-migration]]"]
---

# Reading Library — Resources DB Index

Consolidated index of every entry that lived in the Notion **📚 Resources** database (`collection://87f22aa2-52ac-4f05-8cd4-3f67e5a4901b`, parent database "Learning"). This database was the second-brain reading queue: books, articles, YouTube lectures, and reference bookmarks tagged by topic with status (Want to read / In Progress / Finished / Postponed) and optional Readwise highlights.

The original Resources DB held entries of several shapes:

1. **Read + annotated** — Kindle books synced via Readwise (40+ highlights, a rating, completion date). Each of these has its own markdown file under `content/media/books/`.
2. **Read, no notes** — finished but no highlights made it through. A lightweight individual file preserves the metadata.
3. **Bookmark only** — an Amazon or YouTube link parked for later. Indexed here, no individual file.
4. **Duplicates** — the Notion DB had many duplicate entries from repeated imports. Resolved to a single row below.

> Companion to [[notion-migration]] (which covered the Notes + Knowledge databases). Together these two hubs preserve the full provenance of the migrated vault.

## Conventions

- **Status** column mirrors the Notion `Status` select (Finished / In Progress / Next Up / Want to read / Unread / Postponed).
- **Score** is the Notion `Score /5` (⭐ count) when the reader rated it.
- **Notes** column points to the Obsidian wikilink if an individual file exists; otherwise "bookmark" means the entry lives only in this index.
- Notion page IDs are included so every entry remains traceable back to the original page after the Notion workspace is decommissioned.

## Books with individual notes

| Title | Author | Status | Score | Notes | Notion ID |
| --- | --- | --- | --- | --- | --- |
| 1% Better Every Day *(talk)* | James Clear | Finished | 5/5 | [[1-percent-better-every-day]] | [199cd503c1114db68f079f7e89413be8](https://www.notion.so/199cd503c1114db68f079f7e89413be8) |
| Atomic Habits | James Clear | Finished | 5/5 | [[atomic-habits]] | [e0a09c29aca04ac79d623b475e6262e6](https://www.notion.so/e0a09c29aca04ac79d623b475e6262e6) |
| Astrophysics for People in a Hurry | Neil deGrasse Tyson | — | — | [[astrophysics-for-people-in-a-hurry]] | *(pre-existing)* |
| Ashtanga Hrdayam | — | — | — | [[ashtanga-hrudayam]] · [[AshtangaHrydayam]] | [9c8462bb2edc4981ad44298c56357fa6](https://www.notion.so/9c8462bb2edc4981ad44298c56357fa6) |
| The Black Swan | Nassim Nicholas Taleb | Want to read | — | [[black-swan]] | [a82a3ad992414cfba00fee6e3ea7279a](https://www.notion.so/a82a3ad992414cfba00fee6e3ea7279a) |
| Benjamin Franklin | Walter Isaacson | Next Up | — | [[benjamin-franklin]] | [ae4093f0a92d4751aacef4803b164dea](https://www.notion.so/ae4093f0a92d4751aacef4803b164dea) |
| Classic Computer Science Problems in Python | David Kopec | — | — | [[classic-cs-problems-in-python]] | [f7fe8cb2aba74ae0bc9fe3af1f186fd7](https://www.notion.so/f7fe8cb2aba74ae0bc9fe3af1f186fd7) |
| Designing Data-Intensive Applications | Martin Kleppmann | Want to read | — | [[designing-data-intensive-applications]] | [b03df36d9e884808b7926396a097b24a](https://www.notion.so/b03df36d9e884808b7926396a097b24a) |
| Early Indians | Tony Joseph | — | — | [[Early Indians]] | *(pre-existing)* |
| The Feynman Lectures on Physics | R. P. Feynman | — | — | [[feynman-lectures-on-physics]] | [c0fe3f28b5c44dd78840afd7f1cdfbd1](https://www.notion.so/c0fe3f28b5c44dd78840afd7f1cdfbd1) |
| The 5AM Club | Robin Sharma | Want to read | — | [[5am-club]] | [02f0ed8781e94a34b1890fe504be289b](https://www.notion.so/02f0ed8781e94a34b1890fe504be289b) |
| Grit | Angela Duckworth | Finished | 4/5 | [[grit]] | [28796b1e4ff24796ace690e9f4767b49](https://www.notion.so/28796b1e4ff24796ace690e9f4767b49) |
| India after Gandhi | Ramachandra Guha | Want to read | — | [[india-after-gandhi]] | [67d9ed115d80443a8c9fab29f8bd8621](https://www.notion.so/67d9ed115d80443a8c9fab29f8bd8621) |
| Maharana Bappa Rawal | — | — | — | [[Maharana Bappa Rawal]] | *(pre-existing)* |
| Meditations | Marcus Aurelius (tr. Gregory Hays) | Want to read | — | [[meditations]] | [f2e18f3938b642709c56bd5ad67dfa01](https://www.notion.so/f2e18f3938b642709c56bd5ad67dfa01) |
| Moonwalking with Einstein | Joshua Foer | Finished (dup) | — | [[moonwalking-with-einstein]] | [9893a1c909474de19716f2f0436307ce](https://www.notion.so/9893a1c909474de19716f2f0436307ce) / [19b41eaa80724ce39cc53d54e720fb3b](https://www.notion.so/19b41eaa80724ce39cc53d54e720fb3b) |
| Navneetakam | — | — | — | [[Navneetakam]] | *(pre-existing)* |
| No Rules Rules | Hastings & Meyer | In Progress | — | [[no-rules-rules]] | [840c2b84ab6c4e078c1dd3f7955e342e](https://www.notion.so/840c2b84ab6c4e078c1dd3f7955e342e) |
| Outliers | Malcolm Gladwell | Finished | 3/5 | [[outliers]] | [acd960943d164bcba61155a34631a2fb](https://www.notion.so/acd960943d164bcba61155a34631a2fb) |
| Range | David Epstein | Want to read | — | [[range]] | [80adfeba46c5493992d7a7ad6e15ecc3](https://www.notion.so/80adfeba46c5493992d7a7ad6e15ecc3) |
| The Ride of a Lifetime | Robert Iger | — | — | [[the-ride-of-a-lifetime]] | [6cf85321e7fd4b75af6a70811595bb9f](https://www.notion.so/6cf85321e7fd4b75af6a70811595bb9f) |
| Shoe Dog | Phil Knight | Finished | 4/5 | [[shoe-dog]] | [e3927a33e2084d76adfbdc6171ec7edb](https://www.notion.so/e3927a33e2084d76adfbdc6171ec7edb) |
| Software Engineering at Google | Winters / Manshreck / Wright | Want to read | — | [[software-engineering-at-google]] | [dd5b716acf9a4838913cafa48cba4012](https://www.notion.so/dd5b716acf9a4838913cafa48cba4012) |
| The Subtle Art of Not Giving a F\*ck | Mark Manson | Finished | 5/5 | [[subtle-art-of-not-giving-a-fck]] | [7c6f18f57f5944aca85e386c05a952b0](https://www.notion.so/7c6f18f57f5944aca85e386c05a952b0) |
| Superintelligence | Nick Bostrom | Want to read | — | [[superintelligence]] | [24b1a5a42f504121a0c45fd3c2c3fe9d](https://www.notion.so/24b1a5a42f504121a0c45fd3c2c3fe9d) |
| Sutrasthana | — | — | — | [[Suthrasthana]] | *(pre-existing)* |
| Understanding Distributed Systems | Roberto Vitillo | Want to read | — | [[understanding-distributed-systems]] | [bb61097f08904fa0b9ea962e8a7030c6](https://www.notion.so/bb61097f08904fa0b9ea962e8a7030c6) |
| What If? | Randall Munroe | Want to read | — | [[what-if]] | [8d96503c6428497693da6d6d27fa311f](https://www.notion.so/8d96503c6428497693da6d6d27fa311f) |
| When Breath Becomes Air | Paul Kalanithi | Next Up | — | [[when-breath-becomes-air]] | [48590333ef9a41849bbe682ef68bcc1b](https://www.notion.so/48590333ef9a41849bbe682ef68bcc1b) |
| Why We Sleep | Matthew Walker | Finished | 5/5 | [[why-we-sleep]] | [7780a2ef31224d4db07f419075cb9846](https://www.notion.so/7780a2ef31224d4db07f419075cb9846) |
| Zero to One | Peter Thiel | Want to read | — | [[zero-to-one]] | [69358d87d1f4497180a16baf7d2b998e](https://www.notion.so/69358d87d1f4497180a16baf7d2b998e) |

## Books — bookmark only (no individual note yet)

These were parked in the Resources DB but never had personal notes, highlights, or a rating in Notion. Kept here as a reading queue rather than expanded into individual stub files.

| Title | Author | Status | Notion ID |
| --- | --- | --- | --- |
| That Will Never Work | Marc Randolph | — | [05c758773273454f82f2ee72d2d77201](https://www.notion.so/05c758773273454f82f2ee72d2d77201) |
| Text book of Swasthavritta | — | — | [cdd55fd0b6384d7096205285bfe434eb](https://www.notion.so/cdd55fd0b6384d7096205285bfe434eb) |
| Practical Ayurveda | — | — | [d76d22731be448e7967a3f24eb03e57c](https://www.notion.so/d76d22731be448e7967a3f24eb03e57c) |
| Something Deeply Hidden | Sean Carroll | — | [408305111a9a42049b7a183287bba0c7](https://www.notion.so/408305111a9a42049b7a183287bba0c7) |
| Quantum Memory (Dominic O'Brien) | Dominic O'Brien | — | [c2f568f1d0054faea7c991f9eb680ad0](https://www.notion.so/c2f568f1d0054faea7c991f9eb680ad0) |
| Elementary Number Theory | David Burton | — | [48f12fabdbf44994a132ba39443976a2](https://www.notion.so/48f12fabdbf44994a132ba39443976a2) |
| Number Theory and its Applications | — | — | [8351e8319e2445a0ba769bc56d326ca6](https://www.notion.so/8351e8319e2445a0ba769bc56d326ca6) |
| Number Theory Introduction | — | — | [9acf3e292f804568b92c68d8212d8d46](https://www.notion.so/9acf3e292f804568b92c68d8212d8d46) |
| Elementary Number Theory with Programming | Lewinter & Meyer | — | [1b7b6431c7f446d3b7fc9c625d71d497](https://www.notion.so/1b7b6431c7f446d3b7fc9c625d71d497) |
| The Universe and Beyond | — | — | [2eb0cd30cab44ad4b1c7955fdc4542d1](https://www.notion.so/2eb0cd30cab44ad4b1c7955fdc4542d1) |
| The Universe in a Nutshell | Stephen Hawking | — | [eb6a8b6891244888a013ae1af571add1](https://www.notion.so/eb6a8b6891244888a013ae1af571add1) |
| The Elegant Universe | Brian Greene | — | [9ad03e8909b44bc881fbf2cde24514a3](https://www.notion.so/9ad03e8909b44bc881fbf2cde24514a3) |
| Patanjali Yoga Sutras (Amazon listing) | — | — | [050300c277a5403a9183e1a53f4a189e](https://www.notion.so/050300c277a5403a9183e1a53f4a189e) |
| *"Book"* (untitled entry) | — | — | [1b2ccbfff3cb45149315a9a06cd2497b](https://www.notion.so/1b2ccbfff3cb45149315a9a06cd2497b) |

## Articles with individual notes

| Title | Topic | Notes | Notion ID |
| --- | --- | --- | --- |
| How to Take Smart Notes (Nat Eliason) | Zettelkasten | [[how-to-take-smart-notes]] | [864eda4e4d4849829e3574ead37c2bb0](https://www.notion.so/864eda4e4d4849829e3574ead37c2bb0) |
| Teach Yourself Computer Science | CS curriculum | [[teach-yourself-computer-science]] | [085e8f6b53ea467c920d08dfce2f0fe8](https://www.notion.so/085e8f6b53ea467c920d08dfce2f0fe8) |
| How to Publish Your Own Python Package on PyPi | Python/ops | [[How to Publish Your Own Python Package on PyPi]] | *(pre-existing)* |
| Machine Learning Is Fun Part 4 — Face Recognition | ML | [[Machine Learning Is Fun Part 4 Modern Face Recognition With Deep Learning]] | *(pre-existing)* |
| RFC 7950 — YANG 1.1 | Networking | [[RFC 7950 - The YANG 1.1 Data Modeling Language]] | *(pre-existing)* |
| RFC 1831 | Networking | [[Rfc1831]] | *(pre-existing)* |
| RFC 793 | Networking | [[Rfc793]] | *(pre-existing)* |
| Algodeck flashcards | Algorithms | [[algodeck-algorithm-flashcards]] | *(from Notes DB)* |
| GPU passthrough (Proxmox) | Homelab | [[gpu-passthrough-proxmox-guide]] | *(from Notes DB)* |
| Habit formation stages | Habits | [[habit-formation-stages]] | *(from Notes DB)* |
| Harmonic Series (UCSC PDF) | Math | [[harmonic-series]] | *(from Notes DB)* |
| Generating Functions — Brilliant | Math | [[generating-functions-brilliant]] | *(from Notes DB)* |
| Markdown Diagrams (GitHub gist) | Tooling | [[markdown-diagrams]] | *(from Notes DB)* |
| Sanskrit Dictionaries (OneTab) | Sanskrit | [[sanskrit-dictionaries]] | *(from Notes DB)* |
| Solve interval-based problems | Algorithms | [[solve-interval-based-problems]] | *(from Notes DB)* |
| Subhashitani | Sanskrit | [[subhashitani]] | *(from Notes DB)* |

## Articles — bookmark only

| Title | Topic | Notion ID |
| --- | --- | --- |
| A Helpful Guide to Reading Better | Reading craft | [3f2d98dc18754b578d0943978a74815f](https://www.notion.so/3f2d98dc18754b578d0943978a74815f) · [d8937ce9b19f4615a0ea521ec70076e7](https://www.notion.so/d8937ce9b19f4615a0ea521ec70076e7) *(dup)* |
| How to read books in Golden age of Content | Reading craft | [ee88d0d0038d4a4a90b3b61f42f0c644](https://www.notion.so/ee88d0d0038d4a4a90b3b61f42f0c644) · [71f3919d245b42dca610e1be403996bd](https://www.notion.so/71f3919d245b42dca610e1be403996bd) *(dup)* |
| Good Books, Math and CSE publications | Reference | [989c81afe3484de49acbf278e88e6960](https://www.notion.so/989c81afe3484de49acbf278e88e6960) |
| How to learn quantum mechanics on your own | Physics | [ceef75556fc44d22991003ea0eebc6bd](https://www.notion.so/ceef75556fc44d22991003ea0eebc6bd) |
| Uncle Bob — The Future of Programming | Software craft | [333c43fb5c98472e93029f65b149dd9d](https://www.notion.so/333c43fb5c98472e93029f65b149dd9d) · [3d222a2aeeaa4dfb8f6a86c5697a3b0e](https://www.notion.so/3d222a2aeeaa4dfb8f6a86c5697a3b0e) *(dup)* |
| 10 Steps to Solving a Programming Problem | Problem solving | [02d3ce093c0541b993d14d03cb216845](https://www.notion.so/02d3ce093c0541b993d14d03cb216845) |
| What is Functional Programming? (InfoWorld) | Programming | [dd9b317bd898468ca318dcead15a885b](https://www.notion.so/dd9b317bd898468ca318dcead15a885b) |
| Competitive Programming Tutorials | Algorithms | [9db29897b7de4fad97f5ba0e8a843d35](https://www.notion.so/9db29897b7de4fad97f5ba0e8a843d35) |
| Object Oriented Programming (8) | OOP | [ad2f260a964945b688795b419f770aaf](https://www.notion.so/ad2f260a964945b688795b419f770aaf) |
| Perlisisms — Epigrams in Programming | Programming aphorisms | [18f5ae3909df4d3f8fcb07ac60a6dd5a](https://www.notion.so/18f5ae3909df4d3f8fcb07ac60a6dd5a) |
| Backtracking: search interview questions | Interviewing | [971bf0ee416c4f0db2599ba33ff2860f](https://www.notion.so/971bf0ee416c4f0db2599ba33ff2860f) |
| Programming workout | Practice | [d525c7033d3349da9a4af96985335695](https://www.notion.so/d525c7033d3349da9a4af96985335695) |
| How to Become a Backend Developer — Learning Path | Career | [d6b8682333e34cca9e0a7587d82f1f88](https://www.notion.so/d6b8682333e34cca9e0a7587d82f1f88) |
| Learn to become a modern backend developer | Career | [3dc7cf72cd8c4a60b765476659a181f3](https://www.notion.so/3dc7cf72cd8c4a60b765476659a181f3) |
| Entire CS Curriculum in 1000 YouTube Videos | CS curriculum | [ddd6e60451134b358e1a714c27b53052](https://www.notion.so/ddd6e60451134b358e1a714c27b53052) |
| Making Effective Decisions and Fewer Errors | Productivity | [6382a7ceec3e49d3a595fabe3d2ccd06](https://www.notion.so/6382a7ceec3e49d3a595fabe3d2ccd06) · [52acabcc598b48eebc6c098b1decc55d](https://www.notion.so/52acabcc598b48eebc6c098b1decc55d) *(dup)* |
| Introduction to PostgreSQL physical storage | Databases | [c853fcc01a99463caef47458033870d9](https://www.notion.so/c853fcc01a99463caef47458033870d9) |
| LEADERSHIP LAB: Craft of Writing Effectively | Writing | [eee5c005b965412cbcb532418714c2ed](https://www.notion.so/eee5c005b965412cbcb532418714c2ed) |
| Accelerated Learning: Learn Faster and Remember More | Learning | [0150558497254c38a81a86d99b1c0f42](https://www.notion.so/0150558497254c38a81a86d99b1c0f42) · [eee39b9e34b941be939b62f802f79fd2](https://www.notion.so/eee39b9e34b941be939b62f802f79fd2) *(dup)* |
| The Science of Memory — Top 10 Techniques | Memory | [fe0f2ea10d2e45778db6e596c8f028e9](https://www.notion.so/fe0f2ea10d2e45778db6e596c8f028e9) |
| Bayesian optimization | ML | [9fd5bdd0e3464bf4bb6658e005c72bc6](https://www.notion.so/9fd5bdd0e3464bf4bb6658e005c72bc6) |
| Building a Second Brain (Forte Labs) | PKM | [a40637e764954fe6afb784b31d28cee1](https://www.notion.so/a40637e764954fe6afb784b31d28cee1) · [89e4d41757e94f009e9797df339d8fa4](https://www.notion.so/89e4d41757e94f009e9797df339d8fa4) *(dup)* |
| The PARA Method (Forte Labs) | PKM | [1d3366b9cac04c8eb55462a37346a35b](https://www.notion.so/1d3366b9cac04c8eb55462a37346a35b) · [b965344003e947caa152b5366bb4c1f5](https://www.notion.so/b965344003e947caa152b5366bb4c1f5) *(dup)* |
| Let's Build a Simple Interpreter (Ruslan's Blog) | Compilers | [4d763d8cb33047149ccc459104a2b9ee](https://www.notion.so/4d763d8cb33047149ccc459104a2b9ee) |
| Things I learnt to become senior SE | Career | [0f8b3213d16f4ffbbbc3fb45c00e9575](https://www.notion.so/0f8b3213d16f4ffbbbc3fb45c00e9575) |
| C — Bit Fields | C | [c18d65fae788427a83e51d87334d3505](https://www.notion.so/c18d65fae788427a83e51d87334d3505) |
| Stochastic Gradient Descent with Python & NumPy (Real Python) | ML | [582f36238a8d4a47831551c4a634b8e9](https://www.notion.so/582f36238a8d4a47831551c4a634b8e9) |
| How to think in graphs (Medium) | Graph theory | [4e90e94141cd4afab7a31a125a434a62](https://www.notion.so/4e90e94141cd4afab7a31a125a434a62) |
| Aryabhata's Mathematics | Indic math | [4953c211d8184f51b2b62c2c0587ff07](https://www.notion.so/4953c211d8184f51b2b62c2c0587ff07) |
| How Richard Feynman's Diagrams Revolutionized Physics (Open Culture) | Physics | [920961304324403e88692a9ec6fc2840](https://www.notion.so/920961304324403e88692a9ec6fc2840) |
| Maheshvara Sutras — Shiva Sutras | Sanskrit | [9b636296a46e4653b3698119dfbcbf8b](https://www.notion.so/9b636296a46e4653b3698119dfbcbf8b) |
| Planetary Linguistics | Linguistics | [cce5ae8c182e440d8d4906d2d8f3c549](https://www.notion.so/cce5ae8c182e440d8d4906d2d8f3c549) |
| Patanjali Yoga Sutras | Yoga | [be33d54417bc4c6e8f0bba6a35ca8b96](https://www.notion.so/be33d54417bc4c6e8f0bba6a35ca8b96) |
| Yoga Sutras — Prathama Adhyaya | Yoga | [ebeaccfa88d24f67afa60afd5594247c](https://www.notion.so/ebeaccfa88d24f67afa60afd5594247c) |
| 7.1: Logarithm Defined as an Integral (LibreTexts) | Math | [8c73b1be036046c18d08d373e5f42a28](https://www.notion.so/8c73b1be036046c18d08d373e5f42a28) |
| The Map of Mathematics | Math | [b12200835fd04839a27ce81ed03c2ced](https://www.notion.so/b12200835fd04839a27ce81ed03c2ced) · [1ab12298f3574449ab9de09d09164313](https://www.notion.so/1ab12298f3574449ab9de09d09164313) *(dup)* |
| Reading Confetti — Number Recognition games | Teaching | [fac0671d967444ffab5efd57d0437646](https://www.notion.so/fac0671d967444ffab5efd57d0437646) |
| The Sunset Illusion | Physics | [d494ca550e47445a96a0a542965de060](https://www.notion.so/d494ca550e47445a96a0a542965de060) |
| Probability: seeing theory | Probability | [346b43dc4463420084149cbd66f7ec0a](https://www.notion.so/346b43dc4463420084149cbd66f7ec0a) |
| Productivity system | Productivity | [16567836feb64adca5a7b201dfabb966](https://www.notion.so/16567836feb64adca5a7b201dfabb966) · [6574f9242ec14ff395b094a7955c2f77](https://www.notion.so/6574f9242ec14ff395b094a7955c2f77) *(dup)* |
| How to eliminate self-doubt | Self-development | [3668737b42ad40b087a659ac494ad95f](https://www.notion.so/3668737b42ad40b087a659ac494ad95f) |
| M2M Day 1 — 12 ridiculously hard challenges | Self-development | [cc65db0370aa45a8b0585e2bf336060b](https://www.notion.so/cc65db0370aa45a8b0585e2bf336060b) · [6409b3a83a28411dbc1c2a4fe1c59780](https://www.notion.so/6409b3a83a28411dbc1c2a4fe1c59780) *(dup)* |
| *"Article"* (untitled entry) | — | [a849c7e8a7ab40c9afca31e43d431ae3](https://www.notion.so/a849c7e8a7ab40c9afca31e43d431ae3) |

## YouTube videos with individual notes

| Title | Notes | Notion ID |
| --- | --- | --- |
| Clean Code Lesson 1 | [[clean-code-lesson-1]] | *(from Notes DB)* |
| Analyzing "find max" algorithm | [[analyzing-find-max-algorithm]] | *(from Notes DB)* |
| Four Forces of the Universe (Michio Kaku) | [[four-forces-of-the-universe-kaku]] | *(from Notes DB)* |
| Folding skills | [[folding-skills]] | *(from Notes DB)* |
| Realtime note detection | [[realtime-note-detection]] | *(from Notes DB)* |
| Sangam — History of Indian Science | [[sangam_history_of_indian_science]] | *(pre-existing)* |
| Astronomy — Measuring Distance to Sun | [[astronomy-measuring-distance-to-sun]] | *(pre-existing)* |
| StarTalk — Time Travel | [[startalk-time-travel]] | *(pre-existing)* |

## YouTube videos — bookmark only

These were parked YouTube bookmarks in the Resources DB. Most belong to study queues (MIT 6.006, CS50, Oxford Maths, Patanjali Yoga Sutras, GR lectures). They are listed here rather than expanded into individual files.

### MIT 6.006 Introduction to Algorithms — Fall 2005 / 2011 lecture playlist

| Lecture | Notion ID |
| --- | --- |
| Lec 4 — Asymptotic Notation | [aa3727ad0eeb40a3aae10822084219f8](https://www.notion.so/aa3727ad0eeb40a3aae10822084219f8) |
| Lec 7 — Hashing | [2b4a00333a1a42bfb01ff4c0c8265353](https://www.notion.so/2b4a00333a1a42bfb01ff4c0c8265353) |
| Lec 10 — Red-Black Trees, Rotations | [979990c014f0450c9400da2092d9d584](https://www.notion.so/979990c014f0450c9400da2092d9d584) |
| Lec 12 — Skip Lists | [898ac17211b0457181e68e530c9f4f7c](https://www.notion.so/898ac17211b0457181e68e530c9f4f7c) |
| Lec 14 — Competitive Analysis, Self-organizing Lists | [197b6111d4e743e1baccf12744a84bc5](https://www.notion.so/197b6111d4e743e1baccf12744a84bc5) |
| Lec 14 — DFS, Topological Sort | [d5dc4693cb164e818271ef99b7d427e1](https://www.notion.so/d5dc4693cb164e818271ef99b7d427e1) |
| Lec 16 — Dijkstra | [64f4d381ebba40bc881b57deba1358ef](https://www.notion.so/64f4d381ebba40bc881b57deba1358ef) |
| Lec 17 — Bellman-Ford | [bed673700e8f4ad8a66f655fef84193c](https://www.notion.so/bed673700e8f4ad8a66f655fef84193c) |
| Lec 18 — Speeding up Dijkstra | [bf1711ac26a248e9b9d599c29a64254c](https://www.notion.so/bf1711ac26a248e9b9d599c29a64254c) |
| Lec 19 — Dynamic Programming I: Fibonacci, Shortest Paths | [6437983b763f4875903728108b01b927](https://www.notion.so/6437983b763f4875903728108b01b927) |
| Lec 20 — Dynamic Programming II: Text Justification, Blackjack | [61b6cd702d7142429190320cec688a08](https://www.notion.so/61b6cd702d7142429190320cec688a08) |
| Lec 23 — Computational Complexity | [882ecf1a0070439eb8d5fb3a62fd9893](https://www.notion.so/882ecf1a0070439eb8d5fb3a62fd9893) |
| MIT courses (index) | [4cfe75f1becd4caa9edfd6d95ae962bb](https://www.notion.so/4cfe75f1becd4caa9edfd6d95ae962bb) |

### Programming / tutorials

| Title | Notion ID |
| --- | --- |
| C Programming Tutorial for Beginners | [aa06fac0ed47405fa5f19482c20d3fc5](https://www.notion.so/aa06fac0ed47405fa5f19482c20d3fc5) |
| Harvard CS50 (2018), Lec 2 — C | [d34966c1497c402ea24becafa1bd03e6](https://www.notion.so/d34966c1497c402ea24becafa1bd03e6) |
| Harvard CS50 (2018), Lec 8 — Flask | [f1633df5e2974b44bcf8ec94d21c11b1](https://www.notion.so/f1633df5e2974b44bcf8ec94d21c11b1) |
| Python NumPy Tutorial for Beginners | [a58e6605d0ee483abb3f61beabb7a20b](https://www.notion.so/a58e6605d0ee483abb3f61beabb7a20b) |
| Python OOP for Beginners | [d7179e728f8f427ca5e81475bebfd0d8](https://www.notion.so/d7179e728f8f427ca5e81475bebfd0d8) |
| Graph Theory Tutorial from Google Engineer | [c7a2a1bd7fba4785b5ee076f6a7ce500](https://www.notion.so/c7a2a1bd7fba4785b5ee076f6a7ce500) |
| Maths for Programmers — Sets and Logic (full course) | [b43d555a73a84917afb5b03ae2a85003](https://www.notion.so/b43d555a73a84917afb5b03ae2a85003) |
| Josh Kaufman — How to Learn Anything Fast | [e23f5a89bcbc48968e7a07d59233bca2](https://www.notion.so/e23f5a89bcbc48968e7a07d59233bca2) |

### Physics / mathematics lectures

| Title | Notion ID |
| --- | --- |
| Feynman's Lost Lecture (ft. 3Blue1Brown) | [25bc66f683ee436a828331b916dc9932](https://www.notion.so/25bc66f683ee436a828331b916dc9932) · [1d0f4e23a4464f2d854ece801c4af194](https://www.notion.so/1d0f4e23a4464f2d854ece801c4af194) *(dup)* |
| Susskind — Quantum Mechanics, String Theory & Black Holes (Lex Fridman) | [2c00d9ab446541f6a495284bbbb3c1a2](https://www.notion.so/2c00d9ab446541f6a495284bbbb3c1a2) |
| Susskind — General Relativity Lec 1 | [011deecef5c34f2c81c1efdce53ae4d9](https://www.notion.so/011deecef5c34f2c81c1efdce53ae4d9) · [0edf194ab91941548f4e110c677c0e9d](https://www.notion.so/0edf194ab91941548f4e110c677c0e9d) *(dup)* |
| Oxford Mathematics 1st-Year — Introductory Calculus | [87efda211ec24ad78f4699b53e853d34](https://www.notion.so/87efda211ec24ad78f4699b53e853d34) · [2eaa3832caee49d6814c0dacfb352314](https://www.notion.so/2eaa3832caee49d6814c0dacfb352314) *(dup)* |
| MIT OCW — Single Variable Calculus | [8f27123214ab4acda2acf0339c9a5814](https://www.notion.so/8f27123214ab4acda2acf0339c9a5814) |
| Oxford Mathematics 2nd-Year — Number Theory: Primitive Roots | [42d027e3057f47f69ca1181ba67834d6](https://www.notion.so/42d027e3057f47f69ca1181ba67834d6) · [e46298d72d5145edafde04615da2f1f1](https://www.notion.so/e46298d72d5145edafde04615da2f1f1) *(dup)* |
| Riemann Hypothesis (Numberphile) | [157dee1d70be4c29a1378886b080f85b](https://www.notion.so/157dee1d70be4c29a1378886b080f85b) |
| StarTalk @ NY Comic Con — Time Travel | [09e6cd42a8d3499a96b7ec9018a1e971](https://www.notion.so/09e6cd42a8d3499a96b7ec9018a1e971) |
| StarTalk Live — Science Is Everywhere (Neil deGrasse Tyson & Brian Greene) | [c0f879381d774f4b82da0f3a1c31f78c](https://www.notion.so/c0f879381d774f4b82da0f3a1c31f78c) |
| String Theory and the End of Space and Time | [226c19a5cafa4e0e980ae7b33a0de704](https://www.notion.so/226c19a5cafa4e0e980ae7b33a0de704) |
| Learn Quantum Computation with Qiskit | [8ffb0800ee61424790a25346acd71168](https://www.notion.so/8ffb0800ee61424790a25346acd71168) |

### Yoga Sutras / Sanskrit lectures

| Title | Notion ID |
| --- | --- |
| Yoga Sutras of Patanjali — Prof. Edwin Bryant | [ae4e6268f15341d192b090b77189874a](https://www.notion.so/ae4e6268f15341d192b090b77189874a) |
| Detailed Patanjali Yoga Sutras — Chapter 1 (States of Meditation) | [a4ba33e1573046cbb625f613a4287777](https://www.notion.so/a4ba33e1573046cbb625f613a4287777) |
| Patanjali Yoga Sutras Slokas PPTs | [7e3fa2fdafba4567bf4e53cb94df8163](https://www.notion.so/7e3fa2fdafba4567bf4e53cb94df8163) |
| The Original PanchaTantra — Sanskrit Audiovisual Book Launch | [e230637a3fac43b9af60831455ac1e39](https://www.notion.so/e230637a3fac43b9af60831455ac1e39) |

## Deduplication notes

The Resources database contained several duplicate pages from repeated imports (common in Notion "Reading list" workflows where a second browser extension import would re-create an existing entry). Duplicates are noted inline as *(dup)* in the tables above — the first-listed ID is the canonical entry; the second is the duplicate. When the Notion workspace is decommissioned, the duplicate pages can be deleted without losing information.

**Article / book duplicates resolved**:
- *A Helpful Guide to Reading Better* × 2
- *How to read books in Golden age of Content* × 2
- *Making Effective Decisions and Fewer Errors* × 2
- *Accelerated Learning* × 2
- *Building a Second Brain* × 2
- *The PARA Method* × 2
- *Productivity system* × 2
- *M2M Day 1* × 2
- *Moonwalking with Einstein* × 2
- *The Map of Mathematics* × 2
- *Uncle Bob — Future of Programming* × 2
- *Feynman's Lost Lecture* × 2
- *Susskind GR Lec 1* × 2
- *Oxford Intro Calculus* × 2
- *Oxford Num Theory Primitive Roots* × 2
- *Elementary Number Theory* × 2
- *Number Theory Introduction* × 2
- *Number Theory and its Applications* × 2
- *1% Better Every Day* × 2

## Totals

- **Books with individual notes:** 29 (includes 6 pre-existing in vault).
- **Books — bookmark only:** 14.
- **Articles with individual notes:** 16 (includes 5 pre-existing RFC/ML/Python docs).
- **Articles — bookmark only:** 42 (counting unique entries; ~51 rows if duplicates kept).
- **Videos with individual notes:** 8 (includes 3 pre-existing).
- **Videos — bookmark only:** 28 unique (~35 rows with dups).
- **Grand total unique entries indexed:** ~137.

## Open threads

- A follow-up sweep could promote the bookmark-only entries with clear thematic value (Uncle Bob's "Future of Programming", Perlisisms, the PARA Method) into individual literature notes, rather than leaving them as one-line index entries.
- The MIT 6.006 playlist would benefit from a single `content/media/videos/mit-6-006-intro-to-algorithms.md` aggregate note pointing to all lecture URLs, rather than 14 separate stubs.
- The Yoga Sutras cluster should be consolidated into the existing `content/domains/patanjali-yoga-sutras/` hub (if present) or a new one.
- The untitled *"Book"* and *"Article"* entries (1b2ccbfff3cb… / a849c7e8a7ab…) in the Resources DB look like accidental creations. Worth inspecting and deleting from Notion before decommission.

## Provenance

- Resources DB: `collection://87f22aa2-52ac-4f05-8cd4-3f67e5a4901b` (parent "Learning" — `0005d8768f284b9aa3be5ba8673595d6`)
- Index enumerated through semantic search calls against the Resources data source on 2026-04-19.
- Companion index: [[notion-migration]] (covers Notes + Knowledge databases).

---

*Built on 2026-04-19 as part of the Notion → Obsidian vault migration. See [[notion-migration]] for the companion hub covering the Notes + Knowledge DBs.*
