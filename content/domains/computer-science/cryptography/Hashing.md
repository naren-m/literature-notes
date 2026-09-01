---
title: "Hashing"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: ["cryptography", "hashing", "integrity"]
status: "complete"
related: ["[[Hash Algorithms]]", "[[Integrity]]", "[[Tampering]]", "[[Checksum]]"]
---

# Hashing

Hashing applies a hash function to input data and produces a fixed-length digest.

The digest is useful for detecting whether data changed. A receiver hashes the data again and compares the result. If an attacker can modify both the data and the digest, a plain hash does not prove who created the data; use a [[Message Authentication Code]] or [[Digital signatures]] for that requirement.

Hashing is different from a [[Checksum]]. A cryptographic hash is designed to resist deliberate attacks, while a checksum is mainly designed to detect accidental corruption.
