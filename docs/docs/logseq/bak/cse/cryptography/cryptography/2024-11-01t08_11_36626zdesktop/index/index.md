---
layout: "default"
title: "Cryptography"
word_count: 541
created: "2025-06-25T14:36:45.441116"
modified: "2025-06-25T14:36:45.441116"
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
  - title: "Docs"
    url: "/topics/docs//"
  - title: "Logseq"
    url: "/topics/docs/logseq//"
  - title: "Bak"
    url: "/topics/docs/logseq/bak//"
  - title: "Cse"
    url: "/topics/docs/logseq/bak/cse//"
  - title: "Cryptography"
    url: "/topics/docs/logseq/bak/cse/cryptography//"
  - title: "Cryptography"
    url: "/topics/docs/logseq/bak/cse/cryptography/cryptography//"
  - title: "2024 11 01T08_11_36626Zdesktop"
    url: "/topics/docs/logseq/bak/cse/cryptography/cryptography/2024-11-01t08_11_36626zdesktop//"
---
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

- [Confidentiality](cse/cryptography/confidentiality/)
- [Integrity](cse/cryptography/integrity/)
- [Availability](cse/cryptography/availability/)

Cryptography has various applications

- X.509 certificates
- [Token Authentication](cse/cryptography/token-authentication/)
- Secure boot
- Blockchain Security
- Root of trust

## Some of Security Attacks

- [Zero Day Attack](cse/cryptography/zero-day-attack/)
- [Side Channel Attack](cse/cryptography/side-channel-attack/)
  - [Cold Boot](cse/cryptography/cold-boot/)
  - [Rowhammer](cse/cryptography/rowhammer/)
- [LOJAX](cse/cryptography/lojax/)
- [DLL Preloading Attack](cse/cryptography/dll-preloading-attack/)

## Catch phrases

- Security by obscurity ?

## Techniques

- [Hashing](cse/cryptography/hashing/)
- [Encryption](cse/cryptography/encryption/)
- [Digital signatures](cse/cryptography/digital-signatures/)
  - "Plain text" -> hash -> *Private Key* -> Digital Signature.
    - This does NOT provide Confidentiality

## Notes

- [STRIDE](logseq/bak/cse/cryptography/stride/2024-11-29t01_57_40582zdesktop/)
- [Fingerprint](cse/cryptography/fingerprint/)
- [Public Key](cse/cryptography/public-key/)
- *Private Key*
- [Data Sensitivity](cse/cryptography/data-sensitivity/)
- [Initialization Vector](cse/cryptography/initialization-vector/)
- [Padding](padding/)
- [Entropy](cse/cryptography/entropy/)
- [Checksum](cse/cryptography/checksum/)
  - [Hashing](cse/cryptography/hashing/) is different from [Checksum](cse/cryptography/checksum/).
- [ECC memory](cse/cryptography/ecc-memory/)
- [Root of trust](cse/cryptography/root-of-trust/)

### Terminology

- [Block Cipher](cse/cryptography/block-cipher/)

#### Block Cipher modes

- [Block Cipher](cse/cryptography/block-cipher/) Modes (chaining modes) are used to combine cipher blocks
  - Electronic Codebook (ECB)L encrypt each block and concatenate the individual results.
  - Cipher Block Chaining (CBC): encrypr the first block with a seed. Initial seed is the[Initialization Vector](cse/cryptography/initialization-vector/). The remaining blocks are encrypted with previous ciphe bloc as the seed

- Cipher Feedback (CFB): a mode where data is being provided in a stream versus a block.
- Counter Feedback Mode (CTR): this mode is the combination of encrypting a counter which is then XOR’d with plain text.

## Cool links

[Cyberthreat map](https://cybermap.kaspersky.com/)
[Live Cyber threat map](https://threatmap.checkpoint.com/)

## Topics

- [LOJAX](cse/cryptography/lojax/) attacks
- [Multifernet](cse/cryptography/multifernet/)
- *Rotate*
- [Encryption](cse/cryptography/encryption/) - Asymmetric Encryption
- [Digital signatures](cse/cryptography/digital-signatures/)
- [HMAC](cse/cryptography/hmac/)
- [Bloom Filter](bloom-filter/)
