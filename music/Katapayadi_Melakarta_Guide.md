# The Katapayadi-Melakarta System

*A Complete Guide to Understanding How Rāga Names Encode Their Scales*

---
- ## The Memory Problem
  
  Ancient Indian scholars faced a practical challenge: how do you transmit long numerical sequences across generations in an oral tradition?
  
  Humans remember meaningful words far better than arbitrary digit strings. So they created a systematic mapping from Sanskrit consonants to digits, allowing any number to be encoded as a pronounceable word or phrase.
  
  ---
- ## The Katapayadi Mapping
  
  Sanskrit consonants are grouped into 4 rows, starting with **ka, ṭa, pa, ya**, with each position mapped to a digit:
  
  | Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 |
  |----------|---|---|---|---|---|---|---|---|---|---|
  | ka-row | ka | kha | ga | gha | ṅa | cha | Cha | ja | jha | ña |
  | ṭa-row | ṭa | ṭha | ḍa | ḍha | ṇa | ta | tha | da | dha | na |
  | pa-row | pa | pha | ba | bha | ma | — | — | — | — | — |
  | ya-row | ya | ra | la | va | śa | sha | sa | ha | — | — |
  
  Multiple letters map to the same digit—this gives flexibility to construct meaningful Sanskrit words while still encoding your target number.
  
  **Key decoding rules:**
- Only consonants attached to vowels count
- For conjunct consonants, typically take the last one
- Read digits in reverse order (Indian convention: least significant digit written first)
  
  ---
- ## The Musical Building Blocks
  
  An octave contains 12 semitones. In Carnatic music, a *sampūrṇa* (complete) rāga must include exactly 7 notes—one from each note-family—in strictly ascending pitch order.
  
  Here are the 7 note-families with their variants:
  
  | Note | Variants | Semitone Positions |
  |------|----------|-------------------|
  | **S** (ṣaḍja) | Fixed | 0 |
  | **R** (ṛṣabha) | R1, R2, R3 | 1, 2, 3 |
  | **G** (gāndhāra) | G1, G2, G3 | 2, 3, 4 |
  | **M** (madhyama) | M1, M2 | 5, 6 |
  | **P** (pañcama) | Fixed | 7 |
  | **D** (dhaivata) | D1, D2, D3 | 8, 9, 10 |
  | **N** (niṣāda) | N1, N2, N3 | 9, 10, 11 |
  
  **Critical observation:** Notice that R2 and G1 occupy the *same* semitone (position 2). Similarly for R3/G2, D2/N1, and D3/N2.
  
  ---
- ## The Ascending Order Constraint
  
  Since each note must be higher in pitch than the previous, certain combinations become impossible.
  
  You can't have R3-G1 because G1 is actually *lower* than R3. You can't have R2-G1 because they're the same pitch.
  
  **Valid R-G combinations** (where G is strictly higher than R):
  
  1. R1-G1
  2. R1-G2
  3. R1-G3
  4. R2-G2
  5. R2-G3
  6. R3-G3
  
  That's exactly **6 valid combinations**.
  
  By the same logic, there are exactly **6 valid D-N combinations**: D1N1, D1N2, D1N3, D2N2, D2N3, D3N3.
  
  ---
- ## Why Exactly 72 Rāgas?
  
  Now we can count all possible complete scales:
  
  > **S (fixed) × R-G (6 choices) × M (2 choices) × P (fixed) × D-N (6 choices)**
  >
  > **= 1 × 6 × 2 × 1 × 6 = 72**
  
  This number isn't arbitrary—it's a mathematical consequence of the constraints.
  
  ---
- ## The Systematic Ordering
  
  The 72 melakarta rāgas are arranged in a specific pattern:
  
  **By M (madhyama):**
- Rāgas 1–36: Use M1
- Rāgas 37–72: Use M2
  
  **Within each half**, the 36 rāgas cycle through R-G and D-N combinations systematically, with R-G changing slower than D-N:
- Rāgas 1-6: R1G1 paired with D1N1, D1N2, D1N3, D2N2, D2N3, D3N3
- Rāgas 7-12: R1G2 paired with the same D-N cycle
- Rāgas 13-18: R1G3 paired with the same D-N cycle
- ...and so on
  
  This systematic arrangement means you can **calculate** any scale from its number—no memorization required.
  
  ---
- ## The Algorithm: Number → Scale
  
  Given a melakarta number (1–72):
- ### Step 1: Determine M
- If number ≤ 36 → M1
- If number > 36 → M2, then subtract 36
- ### Step 2: Determine R-G and D-N
- Divide the adjusted number by 6
- If remainder = 0: D-N is the 6th combination, R-G is the quotient-th combination
- If remainder ≠ 0: D-N is the remainder-th combination, R-G is the (quotient+1)-th combination
  
  **Combination numbering:**
- R-G: 1=R1G1, 2=R1G2, 3=R1G3, 4=R2G2, 5=R2G3, 6=R3G3
- D-N: 1=D1N1, 2=D1N2, 3=D1N3, 4=D2N2, 5=D2N3, 6=D3N3
  
  ---
- ## The Naming Convention
  
  Venkatamakhi's genius: **encode the rāga number directly in its name** using Katapayadi.
  
  **To decode a rāga name:**
  
  1. Take the first two consonants
  2. Map each to its Katapayadi digit
  3. Reverse the two digits
  4. Result = rāga number
  
  ---
- ## Worked Example: Shanmukhapriya
- ### Step 1: Name → Number
- First consonant: **sha** = 6
- Second consonant: **mu** (ma-group) = 5
- Digits: 6, 5 → Reversed: **56**
- ### Step 2: Number → Scale
- 56 > 36 → Uses **M2**
- 56 − 36 = 20
- 20 ÷ 6 = quotient 3, remainder 2
- Remainder ≠ 0, so:
	- R-G = (3+1) = 4th combination → **R2G2**
	- D-N = 2nd combination → **D1N2**
	  
	  > **Final scale: S R2 G2 M2 P D1 N2 S**
	  
	  ---
- ## Another Example: Kharaharapriya
- ### Name → Number
- **kha** = 2
- **ra** = 2
- Digits: 2, 2 → Reversed: **22**
- ### Number → Scale
- 22 ≤ 36 → Uses **M1**
- 22 ÷ 6 = quotient 3, remainder 4
- R-G = 4th combination → **R2G2**
- D-N = 4th combination → **D2N2**
  
  > **Final scale: S R2 G2 M1 P D2 N2 S**
  
  ---
- ## Why This System Is Elegant
  
  | Property | Benefit |
  |----------|---------|
  | **Self-documenting** | The name *is* the formula—you never need external reference |
  | **Calculable** | Learn one algorithm instead of memorizing 72 scales |
  | **Error-correcting** | Forgot the scale? Recalculate from the name |
  | **Compact** | 7 notes encoded in 2 consonants |
  | **Culturally natural** | Uses Sanskrit, fitting seamlessly into the tradition |
  
  ---
- ## Summary
  
  This system transforms what could be a brute-force memorization task into an elegant computational process. The rāga name contains everything you need to reconstruct its scale:
  
  > **[[RĀGA]] NAME → [[KATAPAYADI]] → NUMBER → ALGORITHM → FULL SCALE**
  
  The 18th-century musicologist Venkatamakhi essentially created a "hash function" centuries before computer science formalized the concept—reducing a memorization problem to an algorithm, then encoding the algorithm's input directly into the object being named.
-