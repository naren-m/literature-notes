---
title: "HMAC"
date: "2026-04-30"
type: "permanent"
category: "Computer Science/Cryptography"
tags: ["cryptography", "authentication", "hashing"]
status: "draft"
related: ["[[Message Authentication Code]]", "[[Hashing]]", "[[Authentication]]"]
---

# HMAC

HMAC = hash seeded with a secret key. A specific way to build a [[Message Authentication Code]].

Two elements:
- [[Hashing]] algorithm
- [[Authentication]] (shared secret)

Plain hash → anyone can compute it. HMAC → only key holders can produce the same tag. Gives [[Integrity]] + origin.

HMAC is NOT encryption. The message stays readable.

Works with a variety of hashing algorithms: md5, sha1, sha224, sha256, sha384, blake2b, blake2s, and others.

Python. `hmac.new(plaintext, password, hashing algorithm)`

```python
import hashlib
import hmac

hmac1 = hmac.new(b'info 1', b'1234', hashlib.md5)
hmac2 = hmac.new(b'info 2', b'1234', hashlib.sha1)
print("MD5", hmac1.hexdigest())
print("SHA1", hmac2.hexdigest())
```
