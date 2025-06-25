---
layout: "default"
title: "Rowhammer"
word_count: 507
created: "2025-06-25T14:36:45.467646"
modified: "2025-06-25T14:36:45.467646"
backlinks:
  - title: "Cryptography"
    url: "cse/cryptography/cryptography/"
  - title: "ECC memory"
    url: "cse/cryptography/ecc-memory/"
  - title: "Side Channel Attack"
    url: "cse/cryptography/side-channel-attack/"
  - title: "Cryptography"
    url: "logseq/bak/cse/cryptography/cryptography/2024-11-01t08_11_36626zdesktop/"
  - title: "Cryptography"
    url: "logseq/bak/cse/cryptography/cryptography/2024-11-29t01_57_40576zdesktop/"
breadcrumbs:
  - title: "Home"
    url: "/"
  - title: "Docs"
    url: "/topics/docs//"
  - title: "Cse"
    url: "/topics/docs/cse//"
  - title: "Cryptography"
    url: "/topics/docs/cse/cryptography//"
  - title: "Rowhammer"
    url: "/topics/docs/cse/cryptography/rowhammer//"
---
---
layout: "default"
title: "Rowhammer"
word_count: 416
created: "2024-11-28T18:24:53.170190"
modified: "2024-11-28T18:24:53.170190"
backlinks:
  - title: "Cryptography"
    url: "cse/cryptography/cryptography/"
  - title: "ECC memory"
    url: "cse/cryptography/ecc-memory/"
  - title: "Side Channel Attack"
    url: "cse/cryptography/side-channel-attack/"
  - title: "Cryptography"
    url: "logseq/bak/cse/cryptography/cryptography/2024-11-01t08_11_36626zdesktop/"
  - title: "Cryptography"
    url: "logseq/bak/cse/cryptography/cryptography/2024-11-29t01_57_40576zdesktop/"
breadcrumbs:
  - title: "Home"
    url: "/"
  - title: "Cse"
    url: "/topics/cse//"
  - title: "Cryptography"
    url: "/topics/cse/cryptography//"
---
# Rowhammer

Row hammer (also written as rowhammer) is a security exploit that takes advantage of an unintended and undesirable side effect in dynamic random-access memory (DRAM) in which memory cells interact electrically between themselves by leaking their charges, possibly changing the contents of nearby memory rows that were not addressed in the original memory access. This circumvention of the isolation between DRAM memory cells results from the high cell density in modern DRAM, and can be triggered by specially crafted memory access patterns that rapidly activate the same memory rows numerous times.[1][2][3]

This is an example of [Side Channel Attack](cse/cryptography/side-channel-attack/)

The row hammer effect has been used in some *privilege escalation* computer security exploits,[2][4][5][6] and network-based attacks are also theoretically possible.[7][8]

Different hardware-based techniques exist to prevent the row hammer effect from occurring, including required support in some processors and types of DRAM memory modules.[9][10]

ECC Memory should be used to prevent


“Necessity is the mother of invention.” – Plato
Rowhammer attacks are a perfect example of this adage. Adversaries are increasingly inventive in finding creative solutions to attack your systems and applications.
In this attack, a program is executed repeatedly on a row of transistors on a memory chip. The row is hammered until electricity leaks into another row and flips some bits. The adversary can combine bit transformations for a larger purpose: to execute malicious code or otherwise attack the system.
This behavior is more predictable with standard RAM. However, this attack has now been replicated with [ECC memory](cse/cryptography/ecc-memory/). Surprise!

Error Correcting Code Memory (ECC memory) is supposedly resilient to Rowhammer attacks. ECC memory detects bit tampering and amazingly corrects the change. This would seem to be an effective mitigation.
ECC is used in sensitive systems, such as financial systems and IoT devices, because this sort of exploitation is especially troublesome.


Here are the steps of a Rowhammer attack on ECC memory:
1. Rowhammer does templating to locate vulnerable bits. This is possible because ECC memory does not detect tampering of three consecutive bits.
2. Access time for unaltered bits versus tampered bits is different. In poker, this is called a tell. Based on this, you know where to hammer.
3. This is not a quick process. However, the process of templating is virtually undetectable. The adversary can map the attack for days, even weeks, before launching the Rowhammer attack.
More detail on Rowhammer attacks on ECC:
https://bit.ly/2U4EYTg