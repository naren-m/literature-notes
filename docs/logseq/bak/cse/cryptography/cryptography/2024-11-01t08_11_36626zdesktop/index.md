---
layout: "default"
title: "Cryptography"
word_count: 280
created: "2024-11-28T18:24:53.207110"
modified: "2024-11-28T18:24:53.207110"
backlinks:
  - title: "Padding"
    url: "padding/"
  - title: "Security Vulnerabilities"
    url: "security/security-vulnerabilities/"
  - title: "Confidentiality"
    url: "cse/cryptography/confidentiality/"
  - title: "STRIDE"
    url: "cse/cryptography/stride/"
  - title: "Token Authentication"
    url: "cse/cryptography/token-authentication/"
  - title: "Encryption"
    url: "cse/cryptography/encryption/"
  - title: "Cryptography Module3 Streaming"
    url: "cse/cryptography/module3/streaming/readme/"
  - title: "STRIDE"
    url: "logseq/bak/cse/cryptography/stride/2024-11-01t08_11_36618zdesktop/"
  - title: "STRIDE"
    url: "logseq/bak/cse/cryptography/stride/2024-11-29t01_57_40582zdesktop/"
breadcrumbs:
  - title: "Home"
    url: "/"
  - title: "Logseq"
    url: "/topics/logseq//"
  - title: "Bak"
    url: "/topics/logseq/bak//"
  - title: "Cse"
    url: "/topics/logseq/bak/cse//"
  - title: "Cryptography"
    url: "/topics/logseq/bak/cse/cryptography//"
  - title: "Cryptography"
    url: "/topics/logseq/bak/cse/cryptography/cryptography//"
---
# Cryptography

Cryptography is the science of keeping secrets, where hashing and encryption are primary components.

Cryptography is the process of encrypting and protecting data so that only the person who has the right secret key can decrypt it. Quantum cryptography is different from traditional cryptographic systems in that it relies on physics, rather than mathematics, as the key aspect of its security model.

Cryptography supports these important security principles. Detials are in [CIA Triad](logseq/bak/cse/cryptography/cia-triad/2024-11-01t08_11_36610zdesktop/)

- [Confidentiality](docs/cse/cryptography/confidentiality/index/)
- [Integrity](docs/cse/cryptography/integrity/index/)
- [Availability](docs/cse/cryptography/availability/index/)

Cryptography has various applications

- X.509 certificates
- [Token Authentication](docs/cse/cryptography/token-authentication/index/)
- Secure boot
- Blockchain Security
- Root of trust

## Some of Security Attacks

- [Zero Day Attack](docs/cse/cryptography/zero-day-attack/index/)
- [Side Channel Attack](docs/cse/cryptography/side-channel-attack/index/)
  - [Cold Boot](docs/cse/cryptography/cold-boot/index/)
  - [Rowhammer](docs/cse/cryptography/rowhammer/index/)
- [LOJAX](docs/cse/cryptography/lojax/index/)
- [DLL Preloading Attack](docs/cse/cryptography/dll-preloading-attack/index/)

## Catch phrases

- Security by obscurity ?

## Techniques

- [Hashing](docs/cse/cryptography/hashing/index/)
- [Encryption](docs/cse/cryptography/encryption/index/)
- [Digital signatures](docs/cse/cryptography/digital-signatures/index/)
  - "Plain text" -> hash -> *Private Key* -> Digital Signature.
    - This does NOT provide Confidentiality

## Notes

- [STRIDE](logseq/bak/cse/cryptography/stride/2024-11-29t01_57_40582zdesktop/)
- [Fingerprint](docs/cse/cryptography/fingerprint/index/)
- [Public Key](docs/cse/cryptography/public-key/index/)
- *Private Key*
- [Data Sensitivity](docs/cse/cryptography/data-sensitivity/index/)
- [Initialization Vector](docs/cse/cryptography/initialization-vector/index/)
- [Padding](docs/padding/index/)
- [Entropy](docs/cse/cryptography/entropy/index/)
- [Checksum](docs/cse/cryptography/checksum/index/)
  - [Hashing](docs/cse/cryptography/hashing/index/) is different from [Checksum](docs/cse/cryptography/checksum/index/).
- [ECC memory](docs/cse/cryptography/ecc-memory/index/)
- [Root of trust](docs/cse/cryptography/root-of-trust/index/)

### Terminology

- [Block Cipher](docs/cse/cryptography/block-cipher/index/)

#### Block Cipher modes

- [Block Cipher](docs/cse/cryptography/block-cipher/index/) Modes (chaining modes) are used to combine cipher blocks
  - Electronic Codebook (ECB)L encrypt each block and concatenate the individual results.
  - Cipher Block Chaining (CBC): encrypr the first block with a seed. Initial seed is the[Initialization Vector](docs/cse/cryptography/initialization-vector/index/). The remaining blocks are encrypted with previous ciphe bloc as the seed

- Cipher Feedback (CFB): a mode where data is being provided in a stream versus a block.
- Counter Feedback Mode (CTR): this mode is the combination of encrypting a counter which is then XOR’d with plain text.

## Cool links

[Cyberthreat map](https://cybermap.kaspersky.com/)
[Live Cyber threat map](https://threatmap.checkpoint.com/)

## Topics

- [LOJAX](docs/cse/cryptography/lojax/index/) attacks
- [Multifernet](docs/cse/cryptography/multifernet/index/)
- *Rotate*
- [Encryption](docs/cse/cryptography/encryption/index/) - Asymmetric Encryption
- [Digital signatures](docs/cse/cryptography/digital-signatures/index/)
- [HMAC](docs/cse/cryptography/hmac/index/)
- [Bloom Filter](docs/bloom-filter/index/)
