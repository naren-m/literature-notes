---
title: "HMAC"
date: 2026-04-30
type: permanent
category: "Computer Science/Cryptography"
tags: [cryptography, authentication, hashing]
status: draft
related: ["[[Message Authentication Code]]", "[[Hashing]]", "[[Authentication]]"]
---

# HMAC

HMAC is a specific way to build a [[Message Authentication Code]] from a cryptographic hash function and a shared secret key.

The hash alone proves only that data maps to a digest. HMAC adds a secret, so only parties that know the key can produce the same authentication tag. That makes it useful for verifying message [[Integrity]] and origin in systems where both sides share a secret.

The important distinction is that HMAC is not encryption. It does not hide the message; it helps detect tampering and authenticate who could have produced the tag.

## Related

- [[Message Authentication Code]]
- [[Hashing]]
- [[Authentication]]
