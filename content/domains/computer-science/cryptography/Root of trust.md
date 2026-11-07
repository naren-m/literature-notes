---
title: "Root of trust"
date: "2026-04-30"
type: "permanent"
category: "Computer Science/Security"
tags: ["security", "firmware", "trust"]
status: "draft"
source: "https://www.highintegritysystems.com/downloads/white_papers/ESM_Security_whitepaper.pdf"
related: ["[[LOJAX]]", "[[Cryptography]]", "[[Zero-Trust]]"]
---

# Root of trust

First thing the system trusts, so it can decide whether to trust the rest.

- Embedded device's first security goal: confirm the device that booted is the correct device, and its software is not compromised. That's the Root of Trust.
- Secure boot: root verifies the next stage before handing over control. Each stage verifies the next → chain from a small trusted base to the running system.
- Root compromised → whole chain means nothing.
- That's why [[LOJAX]] is scary. It hits the layer the OS stands on but can't inspect from above.
- [[Cryptography]], [[Zero-Trust]]

## Reference

https://www.highintegritysystems.com/downloads/white_papers/ESM_Security_whitepaper.pdf
