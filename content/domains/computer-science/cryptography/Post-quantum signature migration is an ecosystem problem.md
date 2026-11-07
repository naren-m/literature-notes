---
title: "Post-quantum signature migration is an ecosystem problem"
date: "2026-04-30"
type: "permanent"
category: "Computer Science/Cryptography"
tags: ["cryptography", "post-quantum-cryptography", "digital-signatures"]
status: "draft"
source: "[[How Quantum Computers Break Encryption: First Principles]]"
related: ["[[Digital signatures]]", "[[Authentication]]", "[[Key exchange]]", "[[Lattice-based encryption]]"]
---

# Post-quantum signature migration is an ecosystem problem

Picking a quantum-resistant signature algorithm is the easy part. The hard part is everything that carries, stores, verifies and caches signatures.

Think about where [[Digital signatures]] actually live. Certificates. Package registries. Update systems. Identity systems. Logs. Protocols. Every one of them was built assuming signatures and public keys are small.

Now make them much bigger, as with [[Lattice-based encryption]] schemes. Suddenly bandwidth, storage, latency, certificate formats, hardware limits and compatibility are all part of the migration. Not just the crypto library.

Compare with [[Key exchange]]. Key exchange can often be negotiated inside a live session: both sides agree, upgrade, done. Signatures don't work like that. They are baked into long-lived ecosystems and trust chains used for [[Authentication]].

So the cryptography can be ready long before the infrastructure around it is. That gap is the real migration problem.
