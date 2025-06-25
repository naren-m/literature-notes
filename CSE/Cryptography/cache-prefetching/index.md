---
layout: "default"
title: "Cache prefetching"
word_count: 535
created: "2024-11-28T18:24:53.149891"
modified: "2024-11-28T18:24:53.149891"
breadcrumbs:
  - title: "Home"
    url: "/"
  - title: "Cse"
    url: "/topics/cse//"
  - title: "Cryptography"
    url: "/topics/cse/cryptography//"
---
# Cache prefetching

It is a technique used by computer processors to boost the execution performance by fetching the Data or Instructions into the local memory "*Cache*"

## Source
<https://en.wikipedia.org/wiki/Cache_prefetching#:~:text=Cache%20prefetching%20is%20a%20technique>,hence%20the%20term%20'prefetch').

## Data vs. instruction cache prefetching

Cache prefetching can either fetch data or instructions into cache.

- Data prefetching fetches data before it is needed. Because data access patterns show less regularity than instruction patterns, accurate data prefetching is generally more challenging than instruction prefetching.
- Instruction prefetching fetches instructions before they need to be executed. The first mainstream microprocessors to use some form of instruction prefetch were the Intel 8086 (six bytes) and the Motorola 68000 (four bytes). In recent years, all high-performance processors use prefetching techniques.

## Hardware vs. software cache prefetching

Cache prefetching can be accomplished either by hardware or by software.[2]

- Hardware based prefetching is typically accomplished by having a dedicated hardware mechanism in the processor that watches the stream of instructions or data being requested by the executing program, recognizes the next few elements that the program might need based on this stream and prefetches into the processor's cache.[3]
- Software based prefetching is typically accomplished by having the compiler analyze the code and insert additional "prefetch" instructions in the program during compilation itself.[4]

## Metrics of cache prefetching

There are three main metrics to judge cache prefetching[2]

### Coverage

Coverage is the fraction of total misses that are eliminated because of prefetching, i.e.

```math
{\displaystyle Coverage={\frac {\text{Cache Misses eliminated by Prefetching}}{\text{Total Cache Misses}}}}{\displaystyle Coverage={\frac {\text{Cache Misses eliminated by Prefetching}}{\text{Total Cache Misses}}}},

where, {\displaystyle {\text{Total Cache Misses}}=({\text{Cache misses eliminated by prefetching}})+({\text{Cache misses not eliminated by prefetching}})}{\displaystyle {\text{Total Cache Misses}}=({\text{Cache misses eliminated by prefetching}})+({\text{Cache misses not eliminated by prefetching}})}
```

### Accuracy

Accuracy is the fraction of total prefetches that were useful - i.e. the ratio of the number of memory addresses prefetched were actually referenced by the program to the total prefetches done.

```math
{\displaystyle {\text{Prefetch Accuracy}}={\frac {\text{Cache Misses eliminated by prefetching}}{({\text{Useless Cache Prefetches}})+({\text{Cache Misses eliminated by prefetching}})}}}{\displaystyle {\text{Prefetch Accuracy}}={\frac {\text{Cache Misses eliminated by prefetching}}{({\text{Useless Cache Prefetches}})+({\text{Cache Misses eliminated by prefetching}})}}}
```

While it appears that having perfect accuracy might imply that there are no misses, this is not the case. The prefetches themselves might result in new misses if the prefetched blocks are placed directly into the cache. Although these may be a small fraction of the total number of misses we might see without any prefetching, this is a non-zero number of misses.

### Timeliness

The qualitative definition of timeliness is how early a block is prefetched versus when it is actually referenced. An example to further explain timeliness is as follows :

Consider a for loop where each iteration takes 3 cycles to execute and the 'prefetch' operation takes 12 cycles. This implies that for the prefetched data to be useful, we must start the prefetch {\displaystyle 12/3=4}{\displaystyle 12/3=4} iterations prior to its usage to maintain timeliness.
