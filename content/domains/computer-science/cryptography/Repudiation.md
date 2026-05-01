---
title: "Repudiation"
date: 2026-04-30
type: permanent
category: "Computer Science/Security"
tags: [security, stride, logging]
status: draft
source: "https://capec.mitre.org/data/definitions/93.html"
related: ["[[STRIDE]]", "[[Digital signatures]]", "[[Authentication]]"]
---

# Repudiation

Repudiation is the security problem where someone can deny an action because the system cannot prove who did it or whether it happened.

In [[STRIDE]], repudiation points to weak evidence: missing audit logs, mutable logs, poor identity binding, or actions that are not signed or otherwise attributable. The risk is not just that an event occurs, but that the record of responsibility cannot be trusted afterward.

Controls include tamper-resistant audit trails, [[Authentication]], timestamps, authorization records, and [[Digital signatures]] when messages or transactions need stronger proof of origin.

## Related

- [[STRIDE]]
- [[Digital signatures]]
- [[Authentication]]
