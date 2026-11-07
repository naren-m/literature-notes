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

[[Confidentiality]] + [[Integrity]] + [[Availability]] = the pillars of security.

- Confidentiality → only the right people can read it. [[Encryption]] gives this.
- Integrity → is the data trustworthy? Changes are detectable. [[Hashing]] confirms integrity.
- Availability → resources and services are there when expected. Threat: [[Denial of Service]], resource exhaustion.

Related, not interchangeable. Encryption does nothing for availability.

[[STRIDE]] = threat categories that attack these properties.
