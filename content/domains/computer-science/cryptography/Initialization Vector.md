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

IV = fresh input to the cipher, so same plaintext → different ciphertext.

- Not a key. Not a secret.
- Predictability is what adversaries feed on. Patterns leak → [[Security Vulnerabilities]].
- Mode decides the rule: unique, unpredictable, or both.
- Reuse an IV where the mode wants unique → plaintext relationships leak. Security gone.
- IV travels with the ciphertext. Handle it exactly as the mode's spec says.
- Used by [[Block Cipher]] modes of [[Encryption]] → protects [[Confidentiality]].
