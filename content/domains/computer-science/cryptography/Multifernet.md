---
title: "Multifernet"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: []
status: "draft"
related: ["[[Cryptography]]", "[[Encryption]]"]
---

# Multifernet

MultiFernet = key rotation for Fernet.

- Encrypt new data with the current key. Old keys stay around to decrypt old data.
- Example: look at [MultiFernet Example](Cryptography/Module4/multi/multi.py)
