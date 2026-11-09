---
title: "Computer Science & Engineering"
date: "2026-05-05"
type: "permanent"
category: "Computer Science"
tags: ["map", "security", "cryptography", "coding-practices", "design-patterns"]
status: "complete"
related: ["[[Cryptography]]", "[[CIA Triad]]", "[[STRIDE]]", "[[Testing Principles]]", "[[Unix philosophy]]"]
---

# Computer Science & Engineering

Map. Start at the top of a section, follow the arrows.

## Start here

1. [[Cryptography]] → the hub.
2. [[CIA Triad]] → what we protect.
3. [[STRIDE]] → how it gets attacked.
4. [[Testing Principles]] → how we keep code honest.

## Cryptography

Protect → [[Confidentiality]] · [[Integrity]] · [[Availability]] ([[CIA Triad]])

- Hide: [[Encryption]], [[Block Cipher]], [[Initialization Vector]], [[Public Key]], [[Key exchange]], [[Multifernet]]
- Prove nothing changed: [[Hashing]], [[Hash Algorithms]], [[Checksum]], [[Fingerprint]]
- Prove who sent it: [[Message Authentication Code]], [[HMAC]], [[Digital signatures]]
- Randomness: [[ENTROPY]]
- Trust: [[Root of trust]], [[Data Sensitivity]], [[Zero-Trust]]
- Formats: [[JSON]]

### Post-quantum

- [[Quantum attacks depend on exploitable mathematical structure]]
- [[Harvest now decrypt later makes key exchange urgent]]
- [[Grover's algorithm weakens symmetric security quadratically]]
- [[Post-quantum signature migration is an ecosystem problem]]
- [[Lattice-based encryption]]
- Source: [[How Quantum Computers Break Encryption First Principles]]

## Threats & attacks

[[STRIDE]] = [[Spoofing]] · [[Tampering]] · [[Repudiation]] · [[Information Disclosure]] · [[Denial of Service]] · [[Elevation of Privilege]]

- Memory: [[Buffer Overflows]], [[Rowhammer]], [[Cold Boot]], [[ECC memory]]
- Side channels: [[Side Channel Attack]], [[Cache prefetching]]
- Supply chain / firmware: [[DLL Preloading Attack]], [[LOJAX]]
- Unknown unknowns: [[Zero Day Attack]], [[Security Vulnerabilities]]

## Who are you?

[[Authentication]] → [[Strong Authentication]], [[Token Authentication]]

## Coding practices

- Tests: [[Testing Principles]], [[Testing Pyramid]], [[Test Driven Dev]]
- Keep it healthy: [[Maintaining code base]], [[Friday cleaning]], [[One percent rule]], [[aggregation of marginal gains]]
- Ideas: [[Unix philosophy]], [[Idempotence]], [[Leaky abstraction]]
- Python: [[Python Decorators]], [[Decorator Pattern]], [[Hello World]]
- Algorithms: [[Dynamic Programming]] → [[DP Practice]]

## Design & systems

- [[design_patterns|Design patterns]], [[DesigningDistributedSystems]]
- Inbox: [[systemdesign inbox]], [[kubernetes]]

## Machine learning & LLMs

- Sequences: [[RNN]] → [[LSTM]]
- LLMs: [[Key-value Cache]], [[Persistent LLM wikis make synthesis compounding]] ← [[LLM Wiki]]

## Across domains

- [[ENTROPY]] ↔ [[Vikalpa]] → [[Comprehensive_Shannon_Entropy_Vikalpa_Research]]

All notes, one line each → [INDEX](../../../INDEX.md)
