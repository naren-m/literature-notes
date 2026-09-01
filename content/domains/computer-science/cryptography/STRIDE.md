---
title: "STRIDE"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: ["security", "threat-modeling"]
status: "complete"
related: ["[[Spoofing]]", "[[Tampering]]", "[[Repudiation]]", "[[Information Disclosure]]", "[[Denial of Service]]", "[[Elevation of Privilege]]", "[[CIA Triad]]"]
---

# STRIDE

**STRIDE** is a threat-modeling checklist. It asks whether a design is exposed to six common threat classes:

- **Spoofing**: pretending to be another identity;
- **Tampering**: changing data or code without authorization;
- **Repudiation**: denying an action when the system cannot provide reliable evidence;
- **Information disclosure**: exposing data to an unauthorized party;
- **Denial of service**: preventing legitimate use; and
- **Elevation of privilege**: gaining permissions beyond what was granted.

Use STRIDE while tracing trust boundaries and data flows. Map each threat to a concrete control and an observable failure signal. The categories support the [[CIA Triad]], but they do not replace detailed risk analysis.
