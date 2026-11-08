---
title: "Side Channel Attack"
date: "2026-04-30"
type: "permanent"
category: "Computer Science/Security"
tags: ["security", "cryptography", "hardware"]
status: "draft"
related: ["[[Cryptography]]", "[[Cache prefetching]]", "[[Rowhammer]]", "[[Buffer Overflows]]", "[[Cold Boot]]"]
---

# Side Channel Attack

Exploit the unintended information exhaust of an app or device. Often the most creative sort of exploitation.

- Usual focus is inputs and outputs. Even for hardware and UEFI.
- But hardware is physical. Power, time, sound leak → hackers read these side effects → sensitive data, even secrets.
- Most common:
  - Timing: time to complete a calculation or algorithm
  - Power analysis: power consumption per calculation or activity
  - Electromagnetic: leaked EM radiation (monitor, IC emissions)
  - Acoustic: sound related to a calculation
  - cache behaviour → [[Cache prefetching]]
  - memory disturbance → [[Rowhammer]]
- Attacker isn't breaking the math. They measure the implementation around it.
- What protects? [[Cryptography]]! [[Encryption]]. But implemented with care: a secure algorithm can still leak through timing, branching, hardware effects.
- Tel Aviv University has done significant research here. e.g. https://bit.ly/3xOfuLt
