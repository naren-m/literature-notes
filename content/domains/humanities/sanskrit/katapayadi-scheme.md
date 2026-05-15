---
title: "kaṭapayādi Scheme — Applied to Melakarta Ragas"
date: 2026-04-22
type: literature
category: "domains/humanities/sanskrit"
tags: [katapayadi, melakarta, carnatic-music, sanskrit, numerology, venkatamakhi, notion-migration]
status: stable
source: "https://www.notion.so/c11f50763bdf466e917a56418c28d025"
external: "https://rksanka.tripod.com/music/katapaya.html"
related: [
  "[[sanskrit-scholarship]]",
  "[[sanskrit-chandas-meters]]",
  "[[maheshvara-sutras]]",
  "[[notion-migration]]"
]
---

# The kaṭapayādi Scheme — applied to Melakarta Rāgas

Migration of the Notion page on the **kaṭapayādi** (क-ट-प-य-आदि) scheme — an ancient Indian consonant-to-digit encoding, applied here to the **72 mēḷakarta rāgas** of Carnatic music. Full article text from rksanka.tripod.com preserved below.

## The kaṭapayādi rule

Used by ancient Indian mathematicians and grammarians, this rule is a tool to **map names to numbers**. The consonants of the Sanskrit alphabet are written as four groups, with *ka, Ta, pa, ya* as the beginning letters of the groups:

```
         1   2   3   4   5   6   7   8   9   0
         ka  kha  ga  gha  ~ma  cha  Cha  ja  jha  ~na
         Ta  Tha  Da  Dha  Na   ta   tha  da  dha  na
         pa  pha  ba  bha  ma
         ya  ra   la  va   Sa   sha  sa   ha
```

Each letter of the group is numbered 1–9, with **0 for the tenth letter**. Thus *ka* is 1, *sa* is 7, *ma* is 5, *na* is 0, and so on.

### Indian place-value convention (crucial!)

In Indian mathematical tradition, the digits of a number are **written left-to-right in increasing order of place value** — the opposite of the Western convention. So to represent 356, use letters in the **6th, 5th, and 3rd positions** of the group — for example **"triSUlaM"** (त्रिशूलम्).

### Interpretation rules

Several variants existed in historical use. The popular scheme:
- For a **conjoint consonant**, use only the **last** consonant.
- Any consonant **not attached to a vowel** is disregarded.

### Example: decoding a verse to find π

The phrase from **Sadratnamālā** (a treatise on astronomy):

> *bhadram budhi siddha janma gaṇita śraddhāḥ mayādbhūpagiḥ*
> भद्रम् बुधि सिद्ध जन्म गणित श्रद्धाः मयाद्भूपगिः

decodes to: **4 2 3 9 7 8 5 3 5 6 2 9 5 1 4 1 3**

which when reversed (to Western convention) gives:

**3 1 4 1 5 9 2 6 5 3 5 8 7 9 3 2 4**

— **π to 17 decimal places** (with the 17th digit being 3 instead of the correct 3 — a transcription slip; π's 17th digit is actually 3, so it's correct). This is readily recognised as the digits of pi — a spectacular demonstration of the scheme's use as a mnemonic.

*(Source: "The Katapayadi Formula and Modern Hashing Technique" by Anand V Raman, in *Computing Science in Ancient India*, edited by T.R.N. Rao and Subhash Kak, published by the Center for Advanced Computer Studies, University of Southwestern Louisiana.)*

## Mēḷakarta rāgas — the Carnatic music connection

The rāgas of Carnatic music are said to be derived from a definite set of **72 rāgas** known as **mēḷakarta** (janaka / sampūrṇa rāgas). Before going further, recall that an octave has **12 tones**, each separated by a semitone, named as 7 notes with variations on some:

| # | Swara | Abbrev | Solfa | Western |
| --- | --- | --- | --- | --- |
| 1 | shaDjamam | S | Doh | C |
| 2 | Suddha rishabham | R1 |  | C# / Db |
| 3 | chatuSruti rishabham / Suddha gāndhāram | R2 / G1 | Re | D |
| 4 | shaTSruti rishabham / sādhāraṇa gāndhāram | R3 / G2 |  | D# / Eb |
| 5 | antara gāndhāram | G3 | Me | E |
| 6 | Suddha madhyamam | M1 | Fa | F |
| 7 | prati madhyamam | M2 |  | F# / Gb |
| 8 | pancamam | P | Sol | G |
| 9 | Suddha dhaivatam | D1 |  | G# / Ab |
| 10 | chatuSruti dhaivatam / Suddha niṣādam | D2 / N1 | La | A |
| 11 | shaTSruti dhaivatam / kaiśika niṣādam | D3 / N2 |  | A# / Bb |
| 12 | kākali niṣādam | N3 | Ti | B |

### Properties of janaka rāgas

(a) Contain all 7 notes of an octave (hence *sampūrṇa*) **exactly once** in the scale.
(b) Tones in the ārōhaṇa must be in ascending order — you cannot pick S, R3, G1… because R3 is higher than G1. No jumps back and forth.
(c) avarōhaṇa contains the same notes as ārōhaṇa in reverse.

Given these, the possible combinations of (R, G) are 6: **R1G1, R1G2, R1G3, R2G2, R2G3, R3G3**. Same for (D, N): 6. Two varieties of M. So **6 × 6 × 2 = 72** possible sampūrṇa rāgas. If arranged in a regular order, we can derive the scale from the number in the list.

### Application of kaṭapayādi to mēḷakarta

**Venkaṭamakhi** in the 18th century is purported to have applied the kaṭapayādi scheme to name the janaka rāgas so that each name **encodes its position** in the mēḷakarta list. Some names already suited; others were modified — e.g. **kalyāṇī** became **mēca-kalyāṇī**, **śaṅkarābharaṇam** became **dhīra-śaṅkarābharaṇam**, etc.

### Decoding rule (Venkaṭamakhi's variant)

Beyond the standard decoding rules, two special cases for the mēḷakarta names:

1. For conjoint consonants, if one of them is from the *ya* group, consider the **first** consonant (not the last, as in the general rule).
2. To get back to Western-style number notation, **reverse** the decoded digits.

### Examples

| Rāga name | First two letters | Digits | Reversed → rāga # |
| --- | --- | --- | --- |
| kharaharapriyā | **kha** = 2, **ra** = 2 | 22 | 22 |
| śaṇmukhapriyā | **ṣa** = 6, **mu** = 5 | 65 | 56 |
| naṭabhairavī | **na** = 0, **Tha** = 2 | 02 | 20 |
| divyamaṇi | **di** = 8, **va** = 4 | 84 | 48 |

## Deriving the scale from the rāga number

Once you have the number:

1. If NUM is **1–36**, the rāga has **M1**; if **37–72**, the rāga has **M2**.
2. If NUM > 36, subtract 36 from it.
3. Divide NUM by 6.
   - If remainder = 0: the **6th** D,N combination occurs, and the **quotient** gives which R,G combination occurs.
   - If remainder ≠ 0: the **remainder** gives which D,N combination occurs, and **quotient+1** gives which R,G combination.

### Worked example — śaṇmukhapriyā

From kaṭapayādi, śaṇmukhapriyā's number is **56**.
56 > 36 → **M2** occurs.
56 − 36 = 20.
20 ÷ 6 = quotient 3, remainder 2.
So **3 + 1 = 4th R,G combination → R2, G2** and **2nd D,N combination → D1, N2**.

**Scale:** S R2 G2 M2 P D1 N2 S

### Worked example — varuṇapriyā

Number = **24**.
24 < 36 → **M1** occurs.
24 ÷ 6 = quotient 4, remainder 0.
So **4th R,G combination → R2, G2** and **6th D,N combination → D3, N3**.

**Scale:** S R2 G2 M1 P D3 N3 S

## Why this is astonishing

Venkaṭamakhi effectively **compressed the entire 72-rāga mēḷakarta system into a naming convention** — any musician who knows the kaṭapayādi rule and the scale-derivation algorithm can reconstruct any rāga's notes from its name alone. It is one of the earliest examples of **error-correcting mnemonic encoding** in any musical or mathematical tradition — a computer-science-adjacent insight from the 18th century, and closely parallel to modern hashing techniques (as Raman's paper notes).

## Cross-references

- **[[sanskrit-scholarship]]** — cluster hub
- **[[sanskrit-chandas-meters]]** — companion: chandas/metre recognition (same "pattern-as-code" concept applied to Sanskrit prosody)
- **[[maheshvara-sutras]]** — another example of pattern-based compression in the Sanskrit tradition (pratyāhāras in grammar)
- **[[notion-migration]]** — master migration hub

## Provenance

Notion page `c11f50763bdf466e917a56418c28d025`, captured under the Music parent page (not directly under Sanskrit Literature, but thematically related — kaṭapayādi is a Sanskrit-linguistic scheme applied to Carnatic music). Source article: rksanka.tripod.com/music/katapaya.html. Migrated on 2026-04-22.

---

*Migrated from Notion on 2026-04-22. See [[sanskrit-scholarship]] and [[notion-migration]].*
