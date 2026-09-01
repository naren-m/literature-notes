---
title: "Lattice-based encryption"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: ["cryptography", "post-quantum-cryptography", "encryption"]
status: "complete"
related: ["[[Encryption]]", "[[Public Key]]", "[[Key exchange]]"]
---

# Lattice-based encryption

Lattice-based cryptography builds public-key systems from hard problems on mathematical lattices, which are regular sets of points in high-dimensional space.

The construction hides a secret using a public problem with carefully controlled noise. The intended user can remove the noise with the private key, while an attacker must solve the underlying lattice problem.

Lattice-based schemes are important in post-quantum cryptography because no practical quantum shortcut comparable to Shor's algorithm is known for the hard lattice problems used by current designs. This is a security assumption, not a proof that every lattice construction is safe.

The main operational trade-off is size. Lattice-based keys, ciphertexts, and signatures can be larger than their RSA or elliptic-curve equivalents, which affects bandwidth, storage, and protocol compatibility.
