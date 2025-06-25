---
layout: "default"
title: "Hashing"
word_count: 283
created: "2025-06-25T14:36:45.467507"
modified: "2025-06-25T14:36:45.467507"
backlinks:
  - title: "Cryptography"
    url: "cse/cryptography/cryptography/"
  - title: "Hash Algorithms"
    url: "cse/cryptography/hash-algorithms/"
  - title: "Block Cipher"
    url: "cse/cryptography/block-cipher/"
  - title: "Digital signatures"
    url: "cse/cryptography/digital-signatures/"
  - title: "Checksum"
    url: "cse/cryptography/checksum/"
  - title: "CIA Triad"
    url: "cse/cryptography/cia-triad/"
  - title: "Cryptography"
    url: "logseq/bak/cse/cryptography/cryptography/2024-11-01t08_11_36626zdesktop/"
  - title: "Cryptography"
    url: "logseq/bak/cse/cryptography/cryptography/2024-11-29t01_57_40576zdesktop/"
  - title: "CIA Triad"
    url: "logseq/bak/cse/cryptography/cia-triad/2024-11-29t01_57_40574zdesktop/"
  - title: "CIA Triad"
    url: "logseq/bak/cse/cryptography/cia-triad/2024-11-01t08_11_36610zdesktop/"
breadcrumbs:
  - title: "Home"
    url: "/"
  - title: "Docs"
    url: "/topics/docs//"
  - title: "Cse"
    url: "/topics/docs/cse//"
  - title: "Cryptography"
    url: "/topics/docs/cse/cryptography//"
  - title: "Hashing"
    url: "/topics/docs/cse/cryptography/hashing//"
---
---
layout: "default"
title: "Hashing"
word_count: 145
created: "2024-11-28T18:24:53.167797"
modified: "2024-11-28T18:24:53.167797"
backlinks:
  - title: "Cryptography"
    url: "cse/cryptography/cryptography/"
  - title: "Hash Algorithms"
    url: "cse/cryptography/hash-algorithms/"
  - title: "Block Cipher"
    url: "cse/cryptography/block-cipher/"
  - title: "Digital signatures"
    url: "cse/cryptography/digital-signatures/"
  - title: "Checksum"
    url: "cse/cryptography/checksum/"
  - title: "CIA Triad"
    url: "cse/cryptography/cia-triad/"
  - title: "Cryptography"
    url: "logseq/bak/cse/cryptography/cryptography/2024-11-01t08_11_36626zdesktop/"
  - title: "Cryptography"
    url: "logseq/bak/cse/cryptography/cryptography/2024-11-29t01_57_40576zdesktop/"
  - title: "CIA Triad"
    url: "logseq/bak/cse/cryptography/cia-triad/2024-11-29t01_57_40574zdesktop/"
  - title: "CIA Triad"
    url: "logseq/bak/cse/cryptography/cia-triad/2024-11-01t08_11_36610zdesktop/"
breadcrumbs:
  - title: "Home"
    url: "/"
  - title: "Cse"
    url: "/topics/cse//"
  - title: "Cryptography"
    url: "/topics/cse/cryptography//"
---
# Hashing

Hashing is the process of converting a given key into another value. A hash function is used to generate the new value according to a mathematical algorithm. The result of a hash function is known as a hash value or simply, a hash.

Hashing -> Security

A good hash function uses a one-way [Hash Algorithms](cse/cryptography/hash-algorithms/), or in other words, the hash cannot be converted back into the original key.

Hashing is a one-way algorithm that creates a fixed length digest (transformation) from input data.
Features of hashing include:
- Hashing is conducted in sequential blocks
- There is no detectable pattern
- The results are both unpredictable and predictable
- Longer digests tend to be more secure


Hashing protects the [Integrity](cse/cryptography/integrity/) of data. With a hash, you can detect tampering

Hashing is different than [Checksum](cse/cryptography/checksum/).



## References

- [What is hashing](https://www.educative.io/answers/what-is-hashing)