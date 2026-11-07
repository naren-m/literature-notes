---
title: "Cryptography"
date: "2025-12-11"
type: "permanent"
category: "CSE/Cryptography"
tags: ["cryptography", "security", "encryption", "hashing"]
status: "complete"
related: ["[[CIA Triad]]", "[[Confidentiality]]", "[[Integrity]]", "[[Availability]]", "[[Encryption]]", "[[Hashing]]", "[[Digital signatures]]", "[[Fingerprint]]", "[[Multifernet]]"]
---

# Cryptography

> The science of keeping secrets through hashing and encryption

Only the one with the right secret key can decrypt. Math + secrets → trust between parties.

Quantum cryptography is different. It relies on physics, not mathematics, for its security.

Supports the [[CIA Triad]]:
- [[Confidentiality]]
- [[Integrity]]
- [[Availability]]

But crypto alone can't give you these. Key storage, identity binding, authorization, implementation, operations still matter.

Security by obscurity ?

## Techniques
- [[Encryption]] → hides content → [[Confidentiality]]
- [[Hashing]] → digest → detects change
  - [[Hashing]] is different from [[Checksum]].
- [[Digital signatures]] → origin + [[Integrity]]
  - "Plain text" -> hash -> Private Key -> Digital Signature.
    - This does NOT provide Confidentiality
- [[Key exchange]] → shared secret for later encryption
- [[Fingerprint]] → compact way to compare big public data, like keys
- [[HMAC]]
- [[Multifernet]] → key rotation for Fernet-encrypted data

## Applications
- X.509 certificates
- [[Token Authentication]]
- Secure boot
- Blockchain Security
- [[Root of trust]]

## Some of Security Attacks
- [[Zero Day Attack]]
- [[Side Channel Attack]]
  - [[Cold Boot]]
  - [[Rowhammer]]
- [[LOJAX]]
- [[DLL Preloading Attack]]

## Notes
- [[STRIDE]]
- [[Public Key]]
- [[Data Sensitivity]]
- [[Initialization Vector]]
- [[Entropy]]
- [[ECC memory]]

## Block Cipher modes
[[Block Cipher]] modes (chaining modes) combine cipher blocks.
- Electronic Codebook (ECB): encrypt each block, concatenate the results.
- Cipher Block Chaining (CBC): encrypt the first block with a seed. Initial seed = [[Initialization Vector]]. Remaining blocks use the previous cipher block as the seed.
- Cipher Feedback (CFB): data provided as a stream instead of blocks.
- Counter mode (CTR): encrypt a counter, XOR it with the plain text.

## Cool links
- [Cyberthreat map](https://cybermap.kaspersky.com/)
- [Live Cyber threat map](https://threatmap.checkpoint.com/)
