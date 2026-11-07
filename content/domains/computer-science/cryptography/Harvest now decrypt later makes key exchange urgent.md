---
title: "Harvest now decrypt later makes key exchange urgent"
date: "2026-04-30"
type: "permanent"
category: "Computer Science/Cryptography"
tags: ["cryptography", "post-quantum-cryptography", "key-exchange"]
status: "draft"
source: "[[How Quantum Computers Break Encryption: First Principles]]"
related: ["[[Key exchange]]", "[[Confidentiality]]", "[[Data Sensitivity]]", "[[Lattice-based encryption]]"]
---

# Harvest now decrypt later makes key exchange urgent

Here is the thing. You don't need a quantum computer to exist today to get hurt by one.

An attacker records encrypted traffic now. Stores it. Waits. The day the session's key agreement becomes breakable, they recover the old session key and decrypt everything they stored. Harvest now, decrypt later.

So the real question is not "when do quantum computers become practical?" It is "how long does this data need to stay secret?" That's why post-quantum [[Key exchange]] is urgent already.

This changes migration priority. Long-lived [[Confidentiality]] → move to quantum-resistant key agreement before the break arrives. Short-lived data can take the slower path. Medical, legal, financial, government, trade secrets → "safe today" doesn't mean "safe for its whole useful life". Same thinking as [[Data Sensitivity]]: protect by impact.

- [[Lattice-based encryption]]
