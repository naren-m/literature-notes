---
title: "Entropy"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: ["cryptography", "information-theory", "randomness"]
status: "complete"
related: ["[[Cryptography]]", "[[Hashing]]", "[[Block Cipher]]", "[[Digital signatures]]", "[[Vikalpa]]"]
---

# Entropy

Entropy = uncertainty. How hard is the next value to guess?

H(X) = -Σ p(x) log₂ p(x)   (Shannon, measured in bits)

- Uniform → max uncertainty. Predictable → low entropy.
- Good entropy: disordered, unpredictable, not discoverable, not repeatable, uniformly distributed.
- [[Cryptography]] eats entropy: keys, nonces, IVs for [[Block Cipher]] modes, salts for password [[Hashing]], fresh randomness per signature in [[Digital signatures]] (DSA / ECDSA).
- Lots of values ≠ secure. If the attacker can predict them, useless.
- Passing statistical tests ≠ cryptographically unpredictable. Estimating entropy and checking source health are separate jobs.

Entropy vs [[Vikalpa]]? Both are about many possible states. Hypothesis only, not an equivalence. Open work in [[Comprehensive_Shannon_Entropy_Vikalpa_Research]].

Ref: RFC 4086, *Randomness Requirements for Security*
