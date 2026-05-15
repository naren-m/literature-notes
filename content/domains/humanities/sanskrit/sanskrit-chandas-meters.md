---
title: "sanskrit/chandas — Code for Recognising Sanskrit Meters"
date: 2026-04-22
type: literature
category: "domains/humanities/sanskrit"
tags: [chandas, sanskrit-meter, prosody, python, github, computational-linguistics, notion-migration]
status: stable
source: "https://www.notion.so/176bb3bfe0ee4937a18ff6ab0f53fe7a"
external: "https://github.com/sanskrit/chandas"
related: [
  "[[sanskrit-scholarship]]",
  "[[katapayadi-scheme]]",
  "[[maheshvara-sutras]]",
  "[[notion-migration]]"
]
---

# sanskrit/chandas — Meter Recognition

Migration of the Notion page bookmarking **github.com/sanskrit/chandas**, a Python package for recognising Sanskrit metres (*chandas*) from transliterated verse text. Covers all four major classes of Sanskrit metrical form.

## What the tool does

Given Sanskrit verse in SLP1 transliteration, the library classifies the metre by scanning each syllable as *laghu* (short) or *guru* (long) and matching the resulting pattern against a JSON database of known metres.

**Supported metrical classes:**
- *sama-vṛtta* — all four *pādas* (quarters) have identical syllable pattern
- *ardha-sama-vṛtta* — odd and even pādas have different patterns
- *viṣama-vṛtta* — all four pādas have different patterns
- *jāti*, including *āryā* — based on *mātrā* (moraic) count rather than syllable pattern

## Origin story

From the README:

> "All of the hard work was done by the sanskrit-programmers group, especially the first implementation by shreevatsa. I've rewritten the code with a more streamlined API, and eventually I may merge it into the sanskrit package."

The `sanskrit-programmers` Google Group (referenced in the thread at `!topic/sanskrit-programmers/8jhfDaawkWI`) was an early community effort by Sanskrit-literate programmers to build computational tooling; this project is one of its outputs.

## Quickstart

```python
from chandas import Classifier
classifier = Classifier.from_json_file('data/data.json')

data = """
 kaScit kAntAvirahaguruRA svADikArapramattaH
 SApenAstaMgamitamahimA varzaBogyeRa BartuH .
 yakzaScakre janakatanayAsnAnapuRyodakezu
 snigDacCAyAtaruzu vasatiM rAmagiryASramezu .. 1 ..
 """

result = classifier.classify(data)
assert result and result.name == u'mandākrāntā'
```

The example verse is the opening of **Kālidāsa's *Meghadūta*** ("Cloud Messenger"), and as expected the classifier identifies it as **mandākrāntā** — the distinctive "slow-stepping" metre Kālidāsa chose for that poem.

## Testing

```bash
py.test test/*.py
```

## Profiling

```bash
python -m cProfile -s cumulative profile.py
```

## Modules

| Module | Responsibility |
| --- | --- |
| `wrappers.py` | Working with input data |
| `padyas.py` | Representing metrical forms |
| `classify.py` | Matching input data against a metrical form |
| `enums.py` | Storing certain kinds of common data |

## JSON format

Each metre is a JSON object with these keys:

- **`name`** — name of the metre (default: lowercase IAST, e.g. `"mandākrāntā"`)
- **`pattern`** — list of syllable-pattern strings using:
  - `'G'` for guru syllables
  - `'L'` for laghu syllables
  - `'.'` for syllables that can be either
  - `'|'` for yati (caesura — currently ignored)
- **`counts`** — (optional) for jāti metres: a list of 4 numbers, the mātrā length of each pāda

If `pattern` has 1 entry, the verse is treated as sama-vṛtta; 2 entries → ardha-sama; 4 entries → viṣama. If `counts` is present, the verse is treated as jāti.

### Examples

```json
{
 "name": "mandākrāntā",
 "pattern": ["GGGG|LLLLLG|GLGGLGG"]
}
```
The classic mandākrāntā pattern: four gurus, caesura, five laghus and a guru, caesura, then G L G G L G G.

```json
{
 "name": "upacitra",
 "pattern": ["LLGLLGLLGLG", "GLLGLLGLLGG"]
}
```
An ardha-sama-vṛtta with distinct odd/even pādas.

```json
{
 "name": "udgatā",
 "pattern": [
   "L L G L G L L L G L",
   "L L L L L G L G L G",
   "G L L L L L L G L L G",
   "L L G L G L L L G L G L G"
 ]
}
```
A viṣama-vṛtta with four different pādas.

```json
{
 "name": "āryā",
 "pattern": [],
 "counts": [12, 18, 12, 15]
}
```
The classic āryā metre defined by its mātrā counts.

## Why this matters

- **Computational access to classical poetry.** Until tools like this existed, identifying a Sanskrit verse's metre required a trained prosodist. Now any Sanskrit text can be run through the classifier to label every verse.
- **Complement to Paninian grammar.** Pāṇini's system handles *morphology* and *syntax*; chandas handles the *prosodic* layer that determines whether a verse is well-formed. The two systems are independent and equally elaborate.
- **Teaching tool.** By turning metre-classification into runnable code, the library lets students learn by experimentation rather than rote pattern-matching.

## SLP1 transliteration

The classifier requires input in **SLP1** (Sanskrit Library Phonetic Basic) transliteration — a one-character-per-phoneme ASCII encoding. SLP1 is preferred over IAST or Harvard-Kyoto for computation because it's unambiguous and single-byte per phoneme. If working with IAST or Devanagari input, transliterate first (e.g. using the `indic-transliteration` Python package).

## Cross-references

- **[[sanskrit-scholarship]]** — cluster hub
- **[[katapayadi-scheme]]** — companion: kaṭapayādi mapped musical rāga names to numbers using the same phoneme-to-code-point idea at the level of Carnatic music rather than Sanskrit metre
- **[[maheshvara-sutras]]** — Paninian grammar foundation (complementary formal system)
- **[[notion-migration]]** — master migration hub

## Provenance

Notion page `176bb3bfe0ee4937a18ff6ab0f53fe7a` under Sanskrit Literature. README of GitHub project `sanskrit/chandas` captured and migrated on 2026-04-22.

---

*Migrated from Notion on 2026-04-22. See [[sanskrit-scholarship]] and [[notion-migration]].*
