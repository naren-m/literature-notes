---
title: "Message Authentication Code"
date: "2026-04-30"
type: "permanent"
category: "Computer Science/Cryptography"
tags: ["cryptography", "authentication", "integrity"]
status: "draft"
related: ["[[HMAC]]", "[[Integrity]]", "[[Authentication]]", "[[Checksum]]", "[[Hashing]]"]
---

# Message Authentication Code (MAC)

MAC = keyed hash. A hash seeded with a secret key both sides share.

- Verifies both [[Integrity]] and identity ([[Authentication]]) of a message.
- Three aspects: create the key → sign the hash → verify the MAC.
- Verifier recomputes the tag with the same key. Mismatch → reject.
- No [[Confidentiality]]. Message in cleartext is still readable by anyone.
- [[HMAC]] = common construction: hash function + secret key.
