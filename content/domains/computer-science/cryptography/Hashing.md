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

Input → hash function → fixed length digest. One-way.

Hashing → Security

- A good hash uses a one-way [[Hash Algorithms|hash algorithm]]. Can't convert the hash back to the original.
- Conducted in sequential blocks.
- No detectable pattern.
- Results are both unpredictable and predictable (same input → same hash).
- Longer digests tend to be more secure.

Hashing protects the [[Integrity]] of data. With a hash, you can detect [[Tampering|tampering]]. Hash again, compare.

But if the attacker can change both data and digest, a plain hash proves nothing about who made it → [[Message Authentication Code]] or [[Digital signatures]].

Hashing is different from [[Checksum]]. Hash resists deliberate attacks. Checksum catches accidental corruption.

## References
- [What is hashing](https://www.educative.io/answers/what-is-hashing)
