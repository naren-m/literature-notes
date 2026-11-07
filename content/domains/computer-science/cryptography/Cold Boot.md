---
title: "Cold Boot"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: []
status: "draft"
related: ["[[side channel attack]]"]
---

# Cold Boot

Imaginative attacks appear every day. Yet another reason for defense in depth.

Cold boot = another [[Side Channel Attack]]. Needs physical access.

- Abrupt shutdown → data in DRAM / SRAM persists for seconds, even minutes.
- Reboot from an OS on a secondary device (usb stick) → dump the memory → pull the secrets.
- Two forms. In one, "cold" is figurative. In the other it is literal. Brrrr...
  - Freeze the chips (liquid nitrogen, freeze spray) → memory erodes slower → more time to read it.
- Doesn't break the crypto algorithm. Goes around it.
- Mostly an inside job. Disgruntled employees.

In one of the episodes of Burn Notice, the lead character's mom does this. Liquid nitrogen on the chip, reads the data off it.
