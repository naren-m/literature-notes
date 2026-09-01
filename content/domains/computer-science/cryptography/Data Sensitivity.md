---
title: "Data Sensitivity"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: ["security", "data-classification", "privacy"]
status: "complete"
related: ["[[Information Disclosure]]", "[[Cryptography]]"]
---

# Data Sensitivity

Data sensitivity is the level of harm that could result if data is exposed, changed, or lost. Classification lets a team choose protection based on impact instead of treating every field the same way.

A simple working scheme is:

- **P1**: highly sensitive data that directly identifies or enables harm to a person, such as government identifiers or payment data;
- **P2**: data that is less direct but can still identify, profile, or help compromise someone; and
- **P3**: data with limited personal impact when disclosed.

The exact labels and examples belong to the organization's policy. A field must not be placed in a lower class merely because it looks harmless in isolation.

Protect sensitive data in all states: at rest, in transit, and in memory. [[Information Disclosure]] is the threat this classification helps prevent; controls may include access limits, encryption, logging, retention rules, and careful redaction.
