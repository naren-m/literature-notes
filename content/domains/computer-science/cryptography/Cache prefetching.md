---
title: "Cache prefetching"
date: "2026-04-30"
type: "permanent"
category: "Computer Science/Computer Architecture"
tags: ["computer-architecture", "performance", "security"]
status: "draft"
source: "https://en.wikipedia.org/wiki/Cache_prefetching"
related: ["[[Side Channel Attack]]", "[[Rowhammer]]", "[[Cryptography]]"]
---

# Cache prefetching

Bring data or instructions into cache before the processor asks for them. Goal = hide memory latency.

- Data vs instruction prefetching. Data is harder, access patterns are less regular. (Intel 8086 had a 6-byte instruction prefetch, Motorola 68000 had 4.)
- Hardware prefetching: processor watches the access stream, guesses the next few elements, pulls them in.
- Software prefetching: compiler inserts extra "prefetch" instructions.
- Bad guess → wasted bandwidth, useful data evicted.

## Metrics

- Coverage = cache misses eliminated by prefetching / total cache misses
- Accuracy = misses eliminated / (useless prefetches + misses eliminated)
  - Perfect accuracy ≠ zero misses. Prefetched blocks can themselves cause new misses.
- Timeliness = how early the block arrives vs when it is actually used.
  - Loop iteration = 3 cycles, prefetch = 12 cycles → start the prefetch 12/3 = 4 iterations ahead.

## Security angle

Cache hit vs miss = timing difference = something an attacker can measure → [[Side Channel Attack]]. A performance trick becomes a leak.

- [[Rowhammer]]
- [[Cryptography]]

Source: https://en.wikipedia.org/wiki/Cache_prefetching
