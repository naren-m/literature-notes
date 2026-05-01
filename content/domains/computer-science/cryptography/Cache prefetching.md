---
title: "Cache prefetching"
date: 2026-04-30
type: permanent
category: "Computer Science/Computer Architecture"
tags: [computer-architecture, performance, security]
status: draft
source: "https://en.wikipedia.org/wiki/Cache_prefetching"
related: ["[[Side Channel Attack]]", "[[Rowhammer]]", "[[Cryptography]]"]
---

# Cache prefetching

Cache prefetching is a performance technique where hardware or software brings data or instructions into cache before the processor asks for them.

The benefit is latency hiding. If the prefetcher predicts correctly, the data is already nearby when execution needs it, so the program avoids a slower memory access. If it predicts poorly, the prefetch can waste bandwidth, evict useful data, or expose access patterns.

Good prefetching balances three properties:

- Coverage: how many would-be cache misses are avoided.
- Accuracy: how many prefetches are actually used.
- Timeliness: whether the data arrives early enough to help but not so early that it is evicted.

The security connection is that caches make behavior observable. Timing differences from cache hits and misses can become inputs to a [[Side Channel Attack]], even when the original optimization was only meant to improve performance.

## Related

- [[Side Channel Attack]]
- [[Rowhammer]]
- [[Cryptography]]
