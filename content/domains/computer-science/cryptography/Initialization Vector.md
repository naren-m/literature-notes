---
title: "Initialization Vector"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: ["cryptography", "encryption"]
status: "complete"
related: ["[[Encryption]]", "[[Block Cipher]]", "[[Confidentiality]]"]
---

# Initialization Vector

An initialization vector (IV) is a value supplied to some encryption modes to make the encryption of the same plaintext depend on fresh input.

An IV is not a secret key. Its required properties depend on the encryption mode: it may need to be unique, unpredictable, or both. Reusing an IV when a mode requires uniqueness can expose plaintext relationships or break security.

The IV is part of the encrypted message's protocol format and must be handled according to the mode's specification.
