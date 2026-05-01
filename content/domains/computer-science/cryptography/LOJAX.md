---
title: "LoJax"
date: 2026-04-30
type: permanent
category: "Computer Science/Security"
tags: [security, firmware, rootkit, uefi]
status: draft
source: "https://attack.mitre.org/groups/G0007/"
related: ["[[Root of trust]]", "[[Zero-Trust]]", "[[Security Vulnerabilities]]"]
---

# LoJax

LoJax is a UEFI rootkit attack that shows why firmware belongs inside the security boundary.

Unlike ordinary malware, a firmware implant can survive operating-system reinstallations because it lives below the OS. LoJax abused the legitimate LoJack/Computrace firmware persistence mechanism and redirected it toward attacker-controlled behavior.

The durable lesson is that persistence below the operating system weakens ordinary detection and recovery assumptions. Secure Boot, firmware update controls, supply-chain trust, and a defensible [[Root of trust]] matter because the OS cannot fully protect itself from compromised firmware underneath it.

## Related

- [[Root of trust]]
- [[Zero-Trust]]
- [[Security Vulnerabilities]]
