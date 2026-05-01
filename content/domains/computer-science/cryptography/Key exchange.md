---
title: "Key exchange"
date: 2026-04-30
type: permanent
category: "Computer Science/Cryptography"
tags: [cryptography, encryption, authentication]
status: draft
related: ["[[Encryption]]", "[[Public Key]]", "[[Cryptography]]", "[[Harvest now decrypt later makes key exchange urgent]]", "[[Quantum attacks depend on exploitable mathematical structure]]"]
---

# Key exchange

Key exchange is the process two parties use to agree on shared cryptographic material over an untrusted channel.

The important distinction is that key exchange is not the same as encrypting the data itself. It sets up the secret or session key that later [[Encryption]] uses. Public-key techniques make this possible because a party can publish a [[Public Key]] while keeping the corresponding private key secret.

This is why quantum attacks against RSA and elliptic-curve cryptography are urgent: they threaten the agreement step that protects future symmetric sessions, even when the data encryption algorithm remains strong.

## Related

- [[Encryption]]
- [[Public Key]]
- [[Cryptography]]
- [[Harvest now decrypt later makes key exchange urgent]]
- [[Quantum attacks depend on exploitable mathematical structure]]
