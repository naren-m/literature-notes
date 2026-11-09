---
title: "Fingerprint"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: ["cryptography", "hashing"]
status: "draft"
related: ["[[digital signatures]]", "[[public key]]", "[[Authentication]]", "[[Cryptography]]"]
---

# Fingerprint

What is a digital fingerprint? Often confused with [[Digital signatures|digital signatures]].

- Fingerprint = hash of a [[Public Key|public key]]. Short ID for bigger data.
- Two parties compare the fingerprint over a trusted channel before accepting the full key → a factor for [[Authentication|authentication]]. Catches key substitution.
- Fingerprint identifies data. Signature proves possession of the private key + protects message integrity.
