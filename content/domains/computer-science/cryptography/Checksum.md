---
title: "Checksum"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: []
status: "draft"
related: ["[[Integrity]]", "[[Hashing]]"]
---

# Checksum

Checksum = lightweight hash. Highly performant and insecure.

Checksum → [[Integrity]]

Not every target of hashing needs a security-level hash like SHA-256.

LOST BITS. Bits lost during some transformation is the frequent scenario for checksums:
- Compressing / decompressing
- Network transmission
- File transfer
- Data transformation

No attacker in these use cases. But [[Integrity]] is still required. MD5 should be enough.

[[Hashing]] is different from Checksum. An attacker who can change the data can change the checksum too. Attacker in the threat model → [[Message Authentication Code]], digital signature, or a digest delivered over a trusted channel.
