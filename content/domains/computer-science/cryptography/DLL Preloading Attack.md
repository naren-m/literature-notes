---
title: "DLL Preloading Attack"
date: "2026-04-30"
type: "permanent"
category: "Computer Science/Security"
tags: ["security", "windows", "vulnerabilities"]
status: "draft"
related: ["[[Elevation of Privilege]]", "[[Security Vulnerabilities]]", "[[STRIDE]]", "[[Cryptography]]"]
---

# DLL Preloading Attack

Stephen King wrote, "Sooner or later, everything old is new again."

Old Windows threat that made a comeback. Simple to implement.

Load a DLL by name, without a fully qualified path → Windows probes for it:
1. Application directory
2. System directory
3. System directory (16-bit)
4. Windows directory
5. Current directory

First similarly named library wins. Attacker drops a trojan DLL earlier in that order → app loads attacker code.

- Often the first step of another attack, like [[Elevation of Privilege]].
- Worked on well-known products, including Internet Explorer (IE7). Story: https://bit.ly/3p5Kt2l
- Dependency loading is part of the trust boundary. Load from explicit trusted paths. No current-directory lookup.

- [[Security Vulnerabilities]]
- [[STRIDE]]

Source: © 2022 Innovation In Software Corporation (course material)
