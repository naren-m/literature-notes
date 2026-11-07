---
title: "Digital signatures"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: []
status: "draft"
related: ["[[Hashing]]", "[[Encryption]]", "[[Public Key]]", "[[Confidentiality]]", "[[Integrity]]", "[[STRIDE]]", "[[Spoofing]]", "[[Tampering]]"]
---

# Digital signatures

Digital Signature = [[Hashing]] + [[Encryption]] (encrypted with Private key, decrypted with [[Public Key|Public key]])

- Asymmetric encryption.
- Sender creates the signature, receiver verifies it.
- Verifies identity of the sender + [[Integrity|integrity]] of the message.
- Does NOT provide [[Confidentiality|Confidentiality]]

Defends against several [[STRIDE]] threats:
- [[Spoofing]]
- [[Tampering]]
- [[Repudiation]]
- [[Information Disclosure|Information disclosure]]* (?) signature does not hide the message

Only as good as the key and identity binding.

## Sender
1. Create a hash of the message
2. Encrypt the hash with the private key. Result = digital signature.
3. Send the signature to the receiver with the message

## Receiver
Before using the plaintext, verify the signature.
1. Hash the plaintext (hash 1)
2. Decrypt the signature and extract the hash (hash 2)
3. Compare. Same → signature verified.
