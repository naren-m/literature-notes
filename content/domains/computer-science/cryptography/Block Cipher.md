---
title: "Block Cipher"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: []
status: "draft"
related: ["[[Encryption]]", "[[Cryptography]]", "[[Hashing]]", "[[Initialization Vector]]"]
---

# Block Cipher

A block cipher is a symmetric [[Encryption]] primitive that transforms fixed-size blocks of data using a secret key.

Because the input may be longer than one block, a mode of operation defines how the blocks are combined. Modes such as CBC use an [[Initialization Vector]] so identical plaintext blocks do not automatically produce identical ciphertext blocks.

![Block Cipher](images/BlockCipher.png)
