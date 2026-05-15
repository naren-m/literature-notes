---
title: "Sanskrit Parsing — Projects-DB Stub"
date: 2026-04-22
type: project-stub
category: "domains/humanities/sanskrit"
tags: [sanskrit-parsing, projects, panini, computational-linguistics, back-burner, notion-migration]
status: stub
source: "https://www.notion.so/"
related: [
  "[[sanskrit-scholarship]]",
  "[[sanskrit-chandas-meters]]",
  "[[sanskrit-dhatus]]",
  "[[maheshvara-sutras]]",
  "[[projects-library]]",
  "[[notion-migration]]"
]
---

# Sanskrit Parsing — Project Stub

Migration of a Notion Projects-DB row for a proposed project titled **"Sanskrit Parsing"**. The Notion page had **no written body** and a status of **"Back Burner"** — it was a captured project idea, not an active workstream. Preserved here as a stub so the intent is not lost.

## What the project would have been

A Sanskrit parser — i.e. software that takes Sanskrit text (Devanagari or transliterated) and produces a structured morphological and syntactic analysis consistent with **Pāṇini's Aṣṭādhyāyī**. The canonical output would be:

1. **Sandhi resolution** — Sanskrit's extensive phonological rules merge word boundaries; the parser must first split a run of *saṃdhi*-joined text back into individual word-forms.
2. **Morphological analysis** — for each word-form, identify the underlying dhātu (verb root) or prātipadika (noun stem), its suffix chain (kṛt / taddhita / sup / tiṅ), gender, number, case/person/tense.
3. **Syntactic analysis** — identify kāraka relations (the Sanskrit equivalent of thematic roles / dependency relations): kartṛ (agent), karma (patient), karaṇa (instrument), sampradāna (recipient), apādāna (source), adhikaraṇa (locus), etc.
4. **Semantic output** — render the analysis in a form usable for translation, search, or study.

## Existing state-of-the-art

If this project were ever picked up, the landscape to survey includes:

- **Gérard Huet's *Sanskrit Heritage* platform** (sanskrit.inria.fr) — the most comprehensive live Sanskrit analyser; does sandhi splitting, morphological tagging, and partial parsing via OCaml.
- **Amba Kulkarni's Saṃsādhanī toolkit** (University of Hyderabad) — a Paninian-style dependency parser in the Indian NLP tradition.
- **The Sanskrit Library** (sanskritlibrary.org) — corpus, reader tools, annotated texts.
- **sanskrit-programmers** Google Group — the community that produced tools like [[sanskrit-chandas-meters]].
- **Modern NLP approaches** — neural approaches by various research groups (Goyal & Huet, Krishna et al.) on sandhi splitting as a seq2seq problem; still weaker than rule-based Paninian systems on morphology.

## Why it is hard

- **Sandhi ambiguity**: *paraṃ + padam* and *para + upādam* are phonetically indistinguishable when written; multiple parses compete.
- **Long compounds**: Sanskrit permits unbounded nominal compounds (samāsa) with no internal whitespace; parsing them requires resolving bracketing ambiguity ($O(C_n)$, the Catalan number).
- **Free word order**: Classical Sanskrit has nearly free word order, so syntax cannot be inferred from position — it requires full kāraka analysis via case inflection.
- **Paninian grammar vs. modern formalism**: Pāṇini's grammar is a *generative* system (rules produce valid forms); parsing runs it in reverse, which requires non-trivial engineering (Huet's *kale-pada* / *kale-vākya* separation is one attempt).

## Why the author likely parked it

This project sits at the intersection of several substantial skill trees — classical Sanskrit grammar, compiler-style parsing, and formal linguistics. Picking it up seriously requires either (a) committing 6–12 months to reading Huet's published papers and Kale's *Higher Sanskrit Grammar*, or (b) joining one of the existing research groups. "Back burner" was a reasonable place to park it.

## Cross-references

- **[[sanskrit-scholarship]]** — cluster hub
- **[[sanskrit-chandas-meters]]** — companion project (same author-community, metrics-recognition layer)
- **[[sanskrit-dhatus]]** — the verbal-root database any parser would depend on
- **[[maheshvara-sutras]]** — the phonological foundation for the pratyāhāra system any parser must implement
- **[[Ashtadhyayi]]** — existing short note on the grammar that would anchor the parser
- **[[projects-library]]** — projects-DB index where this row lives
- **[[notion-migration]]** — master migration hub

## Provenance

Notion Projects-DB row. Page body was blank; status "Back Burner". Preserved as a stub on 2026-04-22 so the project idea is discoverable from this vault.

---

*Migrated from Notion on 2026-04-22. See [[sanskrit-scholarship]], [[projects-library]], [[notion-migration]].*
