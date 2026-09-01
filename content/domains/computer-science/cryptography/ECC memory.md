---
title: "ECC memory"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: []
status: "draft"
related: ["[[Rowhammer]]", "[[Tampering]]"]
---

# ECC memory

Error-correcting code (ECC) memory detects some bit errors and can correct some of them before they affect the program.

This can reduce the impact of [[Rowhammer]]-induced bit flips, but it is not a complete defense. ECC is useful where silent memory corruption could affect sensitive systems.
