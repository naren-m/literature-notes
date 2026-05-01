---
title: "Root of trust"
date: 2026-04-30
type: permanent
category: "Computer Science/Security"
tags: [security, firmware, trust]
status: draft
source: "https://www.highintegritysystems.com/downloads/white_papers/ESM_Security_whitepaper.pdf"
related: ["[[LOJAX]]", "[[Cryptography]]", "[[Zero-Trust]]"]
---

# Root of trust

A root of trust is the first component a system relies on to decide whether later components should be trusted.

In secure boot flows, that root verifies the next stage before handing over control. Each stage then verifies the next one, creating a chain from a small trusted base to the running system. If the root is compromised, the rest of the chain loses meaning.

This is why firmware attacks such as [[LOJAX]] are serious: they target the layer that the operating system depends on but cannot fully inspect from above.

## Related

- [[LOJAX]]
- [[Cryptography]]
- [[Zero-Trust]]
