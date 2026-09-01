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

Entropy measures uncertainty in a random variable. For a variable (X) with possible values (x), Shannon entropy is:

\[
H(X) = -\sum_x p(x)\log_2 p(x)
\]

The result is measured in bits. A uniform variable has more uncertainty than a variable whose next value is easy to predict.

Cryptographic systems need unpredictable input when generating keys, nonces, initialization vectors, and password salts. A source can produce many values and still be insecure if an attacker can predict those values.

Statistical tests can find obvious bias, but passing a test does not prove that a source is cryptographically unpredictable. Entropy estimation and source health checks are separate parts of the design.

The comparison between information entropy and [[Vikalpa]] is a research hypothesis, not an equivalence between cryptographic randomness and mental states. See [[Comprehensive_Shannon_Entropy_Vikalpa_Research]] for that unresolved work.

## Reference

- RFC 4086, *Randomness Requirements for Security*
