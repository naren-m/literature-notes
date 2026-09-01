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

Cryptography uses mathematical techniques and secrets to protect information and establish trust between parties.

Its main building blocks have different responsibilities:

- [[Encryption]] protects [[Confidentiality]] by hiding content.
- [[Hashing]] creates a digest that can help detect changes.
- [[Digital signatures]] help verify origin and [[Integrity]].
- [[Key exchange]] establishes secret material for later encryption.
- [[Fingerprint]] provides a compact way to compare larger public data such as keys.
- [[Multifernet]] is an example of key rotation for Fernet-encrypted data.

Cryptography supports the three security properties in the [[CIA Triad]], but it cannot provide them by itself. Key storage, identity binding, authorization, implementation behavior, and operational controls still matter.

The main threats and failure modes in this vault include [[Zero Day Attack]], [[Side Channel Attack]], [[Cold Boot]], [[Rowhammer]], [[LOJAX]], and [[DLL Preloading Attack]].
