---
title: "Repudiation"
date: "2026-04-30"
type: "permanent"
category: "Computer Science/Security"
tags: ["security", "stride", "logging"]
status: "draft"
source: "https://capec.mitre.org/data/definitions/93.html"
related: ["[[STRIDE]]", "[[Digital signatures]]", "[[Authentication]]"]
---

# Repudiation

You cannot prove that a transaction took place between two entities.

- Repudiation = rejection of a proposal or idea. Here: "I didn't do that."
- Compromise of non-repudiation. (Trying to hide who we are). The R in [[STRIDE]].
- Attack: system doesn't track and log users' actions properly → attacker forges or changes who did what. Log files become invalid or misleading. Like spoofing mail in someone else's name.
- Root cause = weak evidence: missing logs, mutable logs, poor identity binding, unsigned actions.
- Defend: tamper-resistant audit trails, [[Authentication]], timestamps, authorization records, [[Digital signatures]] for stronger proof of origin.
- Related vulnerability categories: Input Validation, Access Control, Logging and Auditing.

## References

- [capec](https://capec.mitre.org/data/definitions/93.html)
- [owasp repudiation](https://owasp.org/www-community/attacks/Repudiation_Attack#:~:text=Description,the%20identification%20of%20new%20actions)
