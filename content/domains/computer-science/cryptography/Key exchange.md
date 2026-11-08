---
title: "Key exchange"
date: "2026-04-30"
type: "permanent"
category: "Computer Science/Cryptography"
tags: ["cryptography", "encryption", "authentication"]
status: "draft"
related: ["[[Encryption]]", "[[Public Key]]", "[[Cryptography]]", "[[Harvest now decrypt later makes key exchange urgent]]", "[[Quantum attacks depend on exploitable mathematical structure]]", "[[Lattice-based encryption]]", "[[Post-quantum signature migration is an ecosystem problem]]"]
---

# Key exchange

Two parties agree on a shared secret over an untrusted channel.

- Key exchange ≠ encryption. It sets up the session key that [[Encryption]] uses later.
- Possible because of [[Public Key]]: publish one half, keep the private half.
- Quantum threat to RSA/ECC hits this step, not AES. Break the agreement → every session it protected is open, even if the data cipher is strong.
- [[Harvest now decrypt later makes key exchange urgent]]
- [[Quantum attacks depend on exploitable mathematical structure]]
- [[Cryptography]]
