---
title: "Message Authentication Code"
date: 2026-04-30
type: permanent
category: "Computer Science/Cryptography"
tags: [cryptography, authentication, integrity]
status: draft
related: ["[[HMAC]]", "[[Integrity]]", "[[Authentication]]"]
---

# Message Authentication Code

A message authentication code, or MAC, is a short tag that lets someone verify that a message came from a party with the shared secret and was not changed in transit.

The MAC does not provide [[Confidentiality]]. Anyone may still read the message if it is sent in cleartext. Its job is [[Integrity]] and [[Authentication]]: the verifier recomputes the tag with the shared key and rejects the message if the tag does not match.

[[HMAC]] is one common MAC construction that combines a hash function with a secret key.

## Related

- [[HMAC]]
- [[Integrity]]
- [[Authentication]]
