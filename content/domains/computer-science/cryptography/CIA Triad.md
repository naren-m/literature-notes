---
title: "CIA Triad"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: ["security", "confidentiality", "integrity", "availability"]
status: "complete"
related: ["[[Confidentiality]]", "[[Integrity]]", "[[Availability]]", "[[STRIDE]]"]
---

# CIA Triad

The **CIA triad** is a simple way to state three security goals:

- **Confidentiality**: only authorized parties can read the data.
- **Integrity**: data and actions remain correct and changes are detectable.
- **Availability**: authorized users can reach the service or data when needed.

The three goals are related but not interchangeable. Encryption mainly supports confidentiality, authentication and integrity controls help detect unauthorized change, and capacity, redundancy, and recovery controls support availability.

[[STRIDE]] is a threat-modeling framework that helps identify attacks against these properties.
