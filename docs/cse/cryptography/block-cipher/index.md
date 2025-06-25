---
layout: "default"
title: "Block Cipher"
word_count: 82
created: "2024-11-28T18:24:53.149728"
modified: "2024-11-28T18:24:53.149728"
backlinks:
  - title: "Cryptography"
    url: "cse/cryptography/cryptography/"
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
# Block Cipher

A block cipher is an algorithm, when applied to a data source, decomposes the input and processes one chunk (block) at a time.

The algorithm processes the blocks in order.
Basically, a block takes nibbles instead of eating an entire meal at one.

Would you like to add some salt to that sandwich? You can always seed your input with a unique value. When mixed in with normal [Hashing](docs/cse/cryptography/hashing/index/), this adds another level of unpredictability.

![Block Cipher](images/BlockCipher.png)