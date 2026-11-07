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

STRIDE (acronym) = categorization of vulnerabilities. A threat-modeling checklist.

- [[Spoofing]]: theft of user credentials → compromise of [[Authentication]]
- [[Tampering]]: unauthorized data modification → compromise of [[Integrity]]
- [[Repudiation]]: repudiation of activity → compromise of non-repudiation. (Trying to hide who we are) #TODO Circular definition fix it.
- [[Information Disclosure]]: unauthorized access to data → compromise of [[Confidentiality]]
- [[Denial of Service]]: prevent correct access to data or services → compromise of [[Availability]]
- [[Elevation of Privilege]]: unauthorized upgrade in privilege → compromise of authorization

Notes:
- These [[Security Vulnerabilities]] hit the core principles of [[Cryptography]], the [[CIA Triad]].
- Use it while tracing trust boundaries and data flows. Category → best practice to defend or mitigate, now and later.
- Checklist, not a risk analysis.
