---
title: "LoJax"
date: "2026-04-30"
type: "permanent"
category: "Computer Science/Security"
tags: ["security", "firmware", "rootkit", "uefi"]
status: "draft"
source: "https://attack.mitre.org/groups/G0007/"
related: ["[[Root of trust]]", "[[Zero-Trust]]", "[[Security Vulnerabilities]]", "[[Cryptography]]"]
---

# LoJax

UEFI ROOTKIT.

- SEDNIT, a cyberattack group, used LoJax against governments in Europe. https://attack.mitre.org/groups/G0007/
- Built on a legit product: Absolute Software LoJack, originally Computrace. Lets you locate a stolen computer. Preinstalled by many vendors, users didn't know. https://bit.ly/3ACevzG
- LoJack lives in UEFI firmware and "calls home" over the network.
- Why it hurts:
  - UEFI is network enabled
  - LoJack is persistent → survives OS reinstall
  - real product → most anti-virus and scanners don't flag it
- Absolute Software's strategy = "Security by obscurity". Rarely enough. They knew about the problems in 2009 and downplayed them for years.
- What SEDNIT did with it:
  - dump system information to a file
  - redirect data from the device to an attacker server
  - save the image of the system firmware
  - write a malicious module into the image, save it back to SPI flash
- Important: Secure Boot may not prevent this attack.
- Lesson: firmware is inside the security boundary. The OS can't protect itself from what runs beneath it → [[Root of trust]], [[Zero-Trust]], [[Security Vulnerabilities]].
