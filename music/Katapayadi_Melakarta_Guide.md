---
title: "The Katapayadi-Melakarta System"
date: "2026-05-05"
type: "research"
category: "Music"
tags: ["music", "carnatic", "ragas", "melakarta", "katapayadi", "chakra", "bhuta-sankhya", "encoding", "mathematics", "combinatorics", "indian-classical-music", "systematic-knowledge", "information-theory", "hierarchical-systems"]
status: "draft"
---

# The Katapayadi-Melakarta System

Rāga name → number → scale.
72 melakartas of [[Carnatic music]]. 12 chakras × 6 rāgas.
Name encodes the number through [[Katapayadi]]. Number encodes the scale.
Nothing to memorize except the rules.

Oral tradition problem: words are easy to remember, digits are not. So encode digits as words.
Same habit of precision as [[Sulba Sutras]] and [[Vaiseshika Darshanam]].

## Katapayadi mapping

| Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 |
|----------|---|---|---|---|---|---|---|---|---|---|
| ka-row | ka | kha | ga | gha | ṅa | cha | Cha | ja | jha | ña |
| ṭa-row | ṭa | ṭha | ḍa | ḍha | ṇa | ta | tha | da | dha | na |
| pa-row | pa | pha | ba | bha | ma | - | - | - | - | - |
| ya-row | ya | ra | la | va | śa | sha | sa | ha | - | - |

Many letters → same digit. That is the freedom to make a meaningful name.

Decoding:
- Take the first two consonants of the name.
- Only consonants attached to vowels count. Conjunct → usually take the last one.
- Map each to a digit.
- Reverse the two digits (least significant first, Indian convention) = melakarta number.

## Why exactly 72

Sampūrṇa rāga = 7 notes, one from each family, strictly ascending. Octave = 12 semitones. [[Nada]] as in [[Sangitaratnakaram]] and [[Brihadesi]] is the ground.

| Note | Variants | Semitone Positions |
|------|----------|-------------------|
| **S** (ṣaḍja) | Fixed | 0 |
| **R** (ṛṣabha) | R1, R2, R3 | 1, 2, 3 |
| **G** (gāndhāra) | G1, G2, G3 | 2, 3, 4 |
| **M** (madhyama) | M1, M2 | 5, 6 |
| **P** (pañcama) | Fixed | 7 |
| **D** (dhaivata) | D1, D2, D3 | 8, 9, 10 |
| **N** (niṣāda) | N1, N2, N3 | 9, 10, 11 |

R2 = G1 in pitch. Same for R3/G2, D2/N1, D3/N2.
Must ascend → R3-G1, R2-G1 invalid.

Valid R-G: R1-G1, R1-G2, R1-G3, R2-G2, R2-G3, R3-G3.
Valid D-N: D1-N1, D1-N2, D1-N3, D2-N2, D2-N3, D3-N3.

> **S (1) x R-G (6) x M (2) x P (1) x D-N (6) = 72 rāgas**

Not arbitrary. 72 is every scale the constraints allow.

## Ordering

- 1-36 → M1 (Śuddha Madhyama). 37-72 → M2 (Prati Madhyama).
- Inside each half, R-G changes slowly; D-N cycles every 6.
- 1-6 = R1-G1 + six D-N. 7-12 = R1-G2 + six D-N. 13-18 = R1-G3 ... then repeat with M2.

## Chakras

Chakra = 6 rāgas sharing S R G M P. Only D, N change.
72 / 6 = 12 chakras.
Names use **Bhūta Saṅkhyā**: an object stands for a count.

| Chakra | Name | Meaning | Why This Number? |
|--------|------|---------|------------------|
| 1 | **Indu** | Moon | One moon |
| 2 | **Netra** | Eyes | Two eyes |
| 3 | **[[Agni]]** | Fire | Three sacred fires: Āhavanīya, Dakṣiṇa, Gārhapatya |
| 4 | **Veda** | Scripture | Four Vedas |
| 5 | **Bāṇa** | Arrow | Five arrows of Manmatha |
| 6 | **Ṛtu** | Season | Six seasons |
| 7 | **Ṛṣi** | Sage | Seven great sages |
| 8 | **Vasu** | Deity | Eight Vasus |
| 9 | **Brahma** | Creator | Nine Brahmas or Prajāpatis |
| 10 | **Diśi** | Direction | Ten directions: eight compass points, up, down |
| 11 | **[[Rudra]]** | [[shiva|Shiva]] | Eleven Rudras |
| 12 | **Āditya** | Sun | Twelve Ādityas or solar months |

Agni chakra → same fire-altar tradition as [[Sulba Sutras]].

Chakras 1-6 = M1, 7-12 = M2. Position inside the half → R-G:

| Position in Half | R-G Combination |
|------------------|-----------------|
| 1 | R1-G1 |
| 2 | R1-G2 |
| 3 | R1-G3 |
| 4 | R2-G2 |
| 5 | R2-G3 |
| 6 | R3-G3 |

- Agni (3rd) → R1-G3-M1.
- Brahma (9th) → R1-G3-M2.
- Diśi (10th) → R2-G2-M2.

### M1 Chakras: Śuddha Madhyama

| Chakra | Name | Rāgas | R-G | D-N Cycle |
|--------|------|-------|-----|-----------|
| 1 | Indu | 1-6 | R1-G1 | D1N1, D1N2, D1N3, D2N2, D2N3, D3N3 |
| 2 | Netra | 7-12 | R1-G2 | D1N1, D1N2, D1N3, D2N2, D2N3, D3N3 |
| 3 | Agni | 13-18 | R1-G3 | D1N1, D1N2, D1N3, D2N2, D2N3, D3N3 |
| 4 | Veda | 19-24 | R2-G2 | D1N1, D1N2, D1N3, D2N2, D2N3, D3N3 |
| 5 | Bāṇa | 25-30 | R2-G3 | D1N1, D1N2, D1N3, D2N2, D2N3, D3N3 |
| 6 | Ṛtu | 31-36 | R3-G3 | D1N1, D1N2, D1N3, D2N2, D2N3, D3N3 |

### M2 Chakras: Prati Madhyama

| Chakra | Name | Rāgas | R-G | D-N Cycle |
|--------|------|-------|-----|-----------|
| 7 | Ṛṣi | 37-42 | R1-G1 | D1N1, D1N2, D1N3, D2N2, D2N3, D3N3 |
| 8 | Vasu | 43-48 | R1-G2 | D1N1, D1N2, D1N3, D2N2, D2N3, D3N3 |
| 9 | Brahma | 49-54 | R1-G3 | D1N1, D1N2, D1N3, D2N2, D2N3, D3N3 |
| 10 | Diśi | 55-60 | R2-G2 | D1N1, D1N2, D1N3, D2N2, D2N3, D3N3 |
| 11 | Rudra | 61-66 | R2-G3 | D1N1, D1N2, D1N3, D2N2, D2N3, D3N3 |
| 12 | Āditya | 67-72 | R3-G3 | D1N1, D1N2, D1N3, D2N2, D2N3, D3N3 |

### Position inside a chakra

| Position | Syllable | Katapayadi Value |
|----------|----------|------------------|
| 1st | pa | 1 |
| 2nd | śrī | 2 |
| 3rd | go | 3 |
| 4th | bhu | 4 |
| 5th | ma | 5 |
| 6th | sha | 6 |

- "Agni-go" = 3rd in Agni = rāga 15, Mayamalavagaula.
- "Bāṇa-bhu" = 4th in Bāṇa = rāga 28, Harikambhoji.

## Number → scale

1. `chakra = ceil(number / 6)`
2. Chakra 1-6 → M1. 7-12 → M2.
3. `position_in_half = ((chakra - 1) mod 6) + 1` → R-G table.
4. `position_in_chakra = ((number - 1) mod 6) + 1` → D-N table.

| Position in Chakra | D-N Combination |
|--------------------|-----------------|
| 1 | D1-N1 |
| 2 | D1-N2 |
| 3 | D1-N3 |
| 4 | D2-N2 |
| 5 | D2-N3 |
| 6 | D3-N3 |

> **S R G M P D N S**

> **RĀGA NAME -> KATAPAYADI -> MELAKARTA NUMBER -> CHAKRA -> FULL SCALE**

## Worked examples

**Shanmukhapriya**
- sha = 6, mu (ma) = 5 → 6, 5 → reversed **56**.
- Chakra 10, Diśi. M2. Position in half 4 → R2-G2.
- `((56 - 1) mod 6) + 1 = 2` → D1-N2.
- **S R2 G2 M2 P D1 N2 S**

**Mayamalavagaula**
- ma = 5, ya = 1 → reversed **15**.
- Chakra 3, Agni. M1. Position 3 → R1-G3.
- `((15 - 1) mod 6) + 1 = 3` → D1-N3.
- **S R1 G3 M1 P D1 N3 S**

**Kharaharapriya**
- kha = 2, ra = 2 → **22**.
- Chakra 4, Veda. M1. Position 4 → R2-G2.
- `((22 - 1) mod 6) + 1 = 4` → D2-N2.
- **S R2 G2 M1 P D2 N2 S**

## Structure

```text
                    72 MELAKARTA RĀGAS
                           |
           +---------------+---------------+
           |                               |
      M1 (Rāgas 1-36)               M2 (Rāgas 37-72)
           |                               |
    +------+------+                 +------+------+
    |      |      |                 |      |      |
  Indu   ...    Ṛtu              Ṛṣi    ...   Āditya
  (1-6)        (31-36)          (37-42)       (67-72)
    |                               |
    +-- 1: Kanakaṅgi (D1N1)        +-- 37: Sālagam (D1N1)
    +-- 2: Ratnāṅgi (D1N2)         +-- 38: Jalārṇavam (D1N2)
    +-- 3: Gānamūrti (D1N3)        +-- 39: Jhālavarāḷi (D1N3)
    +-- 4: Vanaspati (D2N2)        +-- 40: Navanītam (D2N2)
    +-- 5: Mānavati (D2N3)         +-- 41: Pāvani (D2N3)
    +-- 6: Tānarūpi (D3N3)         +-- 42: Raghupriya (D3N3)
```

| Layer | What It Encodes | Encoding System |
|-------|-----------------|-----------------|
| Chakra name | Group number, hence M type and R-G | Bhūta Saṅkhyā |
| Rāga name | Exact position from 1-72 | Katapayadi consonant-digit mapping |
| Position in chakra | D-N pair | Six-position cycle |

- Name = index. Two consonants + rules → full 7-note scale.
- Chakra and number cross-check each other. Built-in redundancy, like a checksum.
- Compression + redundancy = [[ENTROPY]] / information theory.
- Venkatamakhi turned memorization into an algorithm.

## Related

- [[Carnatic music]]
- [[Katapayadi]]
- [[Nada]]
- [[Sangitaratnakaram]]
- [[Brihadesi]]
- [[Agni]]
- [[Rudra]]
- [[shiva]]
- [[Sulba Sutras]]
- [[Vaiseshika Darshanam]]
- [[ENTROPY]]

## Tags

#music #carnatic #ragas #melakarta #katapayadi #chakra #bhuta-sankhya #encoding #mathematics #combinatorics #indian-classical-music #systematic-knowledge #information-theory #hierarchical-systems
