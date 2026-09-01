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

A digital signature lets a receiver verify the origin and [[Integrity]] of a message using asymmetric cryptography.

The sender signs a digest of the message with a private key. The receiver uses the matching [[Public Key]] to verify the signature against a newly calculated digest.

Digital signatures do not provide [[Confidentiality]]. They help defend against [[Spoofing]], [[Tampering]], and [[Repudiation]] when the key and identity binding are managed correctly.
