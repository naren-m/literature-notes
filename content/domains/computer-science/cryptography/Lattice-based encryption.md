---
title: "Lattice-based encryption"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: ["cryptography", "post-quantum-cryptography", "encryption"]
status: "complete"
related: ["[[Encryption]]", "[[Public Key]]", "[[Key exchange]]", "[[Harvest now decrypt later makes key exchange urgent]]", "[[Post-quantum signature migration is an ecosystem problem]]", "[[Quantum attacks depend on exploitable mathematical structure]]"]
---

# Lattice-based encryption

Lattice = regular grid of points, a pattern repeated forever. Like tiles on a bathroom floor.

```
  •       •       •       •       •
      •       •       •       •       •
  •       •       •       •       •
      •       •       •       •       •
```

Hard problem: find the shortest vector in the lattice.

```
2D lattice:    Easy (you can see it)
3D lattice:    Still manageable
500D lattice:  Astronomically hard
```

- Shortest Vector Problem (SVP), Learning With Errors (LWE).
- Can't visualize 500 dimensions. Grid is slightly "noisy". More paths than atoms in the universe.
- No known shortcut. Not classical, not quantum.

[[Encryption]] idea:

```
Private Key:  Clean lattice structure
Public Key:   Noisy version of that structure
Encryption:   Hide message in the noise
Decryption:   Use clean structure to remove noise → reveal message
```

Publish the noisy one as the [[Public Key]]. Only you know the clean one.

| Problem Type       | Quantum Attack                                    |
| ------------------ | ------------------------------------------------- |
| Factoring (RSA)    | Shor's algorithm finds the structure → **Broken** |
| Discrete log (ECC) | Shor's algorithm finds the structure → **Broken** |
| Lattice problems   | No known quantum shortcut → **Safe**              |

- RSA/ECC = needle in a haystack, but quantum computers have a magnet.
- Lattice = needle in a haystack in 500 dimensions. No magnet works here.
- "Safe" = assumption, not proof. No shortcut *known*.

Trade-off: bigger keys and signatures.

| Scheme              | Public Key + Signature |
| ------------------- | ---------------------- |
| Ed25519 (ECC)       | ~96 bytes              |
| ML-DSA-44 (Lattice) | ~3,800 bytes           |

Quantum safety costs extra bytes → bandwidth, storage, protocol compatibility. Matters for [[Key exchange]] and signatures.
