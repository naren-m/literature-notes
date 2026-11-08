---
title: "Block Cipher"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: []
status: "draft"
related: ["[[Encryption]]", "[[Cryptography]]", "[[Hashing]]", "[[Initialization Vector]]", "[[ENTROPY]]", "[[Grover's algorithm weakens symmetric security quadratically]]", "[[Hash Algorithms]]"]
---

# Block Cipher

Symmetric [[Encryption]] primitive in [[Cryptography]]. Breaks the input into fixed-size chunks (blocks) and processes one block at a time, in order, with a secret key.

Basically, a block cipher takes nibbles instead of eating the entire meal at once.

- Input longer than one block? A mode of operation decides how the blocks are combined (ECB, CBC, CFB, CTR → see [[Cryptography]]).
- Would you like some salt with that sandwich? Seed the input with a unique value → [[Initialization Vector]]. Same trick as salting in [[Hashing]], one more level of unpredictability.
- CBC + IV → identical plaintext blocks don't give identical ciphertext blocks.

![Block Cipher](images/BlockCipher.png)
