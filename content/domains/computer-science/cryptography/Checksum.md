---
title: "Checksum"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: []
status: "draft"
related: ["[[Integrity]]", "[[Hashing]]"]
---

# Checksum

Checksums are small values used to detect accidental changes to data.

They are useful after compression, network transmission, file transfer, or another data transformation. The receiver calculates the checksum again and compares it with the original value. A mismatch shows that the data changed.

A checksum is not a security control. An attacker who can change the data can usually change the checksum too. Use a [[Message Authentication Code]], a digital signature, or a cryptographic digest delivered through a trusted channel when an attacker is part of the threat model.
