---
title: "Resurrecting Duckling model"
date: 2020-07-22
type: research
category: "CSE/security"
tags: [security, iot, tofu, rfc8366, ownership-transfer]
status: incomplete
source: "Notion Knowledge DB; see RFC 8366 and the original Stajano/Anderson 'Resurrecting Duckling' paper"
related: []
---

# Resurrecting Duckling model

Captured notes on the Resurrecting Duckling security model for IoT device ownership transfer. Classified as research because the note is exploratory, short, and unresolved — it references follow-up material and leaves open questions.

## Core idea

The Resurrecting Duckling model addresses **ownership transfer** for IoT devices. A device, after a change in ownership, can often be easily reset — and whoever resets it can claim ownership.

When the duckling is "resurrected" (reset), it imprints on whoever it sees first and trusts that party as its "mother."

In a nutshell, this gives IoT devices a security model built around imprinting at first power-on / first reset.

## References

- Original paper: *The Resurrecting Duckling: Security Issues for Ad-hoc Wireless Networks* — Stajano & Anderson.
- RFC 8366 uses this model to describe the imprint-stage vulnerability: during first provisioning, the device cannot yet be protected because it has no credentials to anchor trust. This is related to the **Trust On First Use (TOFU)** pattern.

## Open threads

- How do modern secure-provisioning schemes (e.g., BRSKI in RFC 8995) bound the Duckling problem?
- How does TOFU compare with attestation-based onboarding in terms of residual risk?
- Original Notion page referenced further bookmarks that did not survive migration — recover those before promoting anything from this note to permanent status.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/8547058e4ebb4446b4468a1367239211). See [[notion-migration]].*
