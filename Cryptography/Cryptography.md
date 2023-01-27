# Cryptography

Cryptography is the science of keeping secrets, where hashing and encryption are primary components.

Cryptography is the process of encrypting and protecting data so that only the person who has the right secret key can decrypt it. Quantum cryptography is different from traditional cryptographic systems in that it relies on physics, rather than mathematics, as the key aspect of its security model.

Cryptography supports these important security principles. Detials are in [[CIA Triad]]

- [[Confidentiality]]
- [[Integrity]]
- [[Availability]]

Cryptography has varios applicaitons

- X.509 certificates
- [[Token Authentication]]
- Secure boot
- Blockchain Security
- Root of trust

## Some of Security Attacks

- [[Zero Day Attack]]
- [[Side Channel Attack]]
  - [[Cold Boot]]
  - [[Rowhammer]]
- [[LOJAX]]
- [[DLL Preloading Attack]]

## Catch phrases

- Security by obscurity ?

## Techniques

- [[Hashing]]
- [[Encryption]]
- [[Digital signatures]]
  - "Plain text" -> hash -> [[Private Key]] -> Digital Signature.
    - This does NOT provide Confidentiality

## Notes

- [[STRIDE]]
- [[Fingerprint]]
- [[Public Key]]
- [[Private Key]]
- [[Data Sensitivity]]
- [[Initialization Vector]]
- [[Padding]]
- [[Entropy]]
- [[Checksum]]
  - [[Hashing]] is different from [[Checksum]].
- [[ECC memory]]
- [[Root of trust]]

### Terminology

- [[Block Cipher]]

#### Block Cipher modes

- [[Block Cipher]] Modes (chaining modes) are used to combine cipher blocks
  - Electronic Codebook (ECB)L encrypt each block and concatenate the individual results.
  - Cipher Block Chaining (CBC): encrypr the first block with a seed. Initial seed is the[[Initialization Vector]]. The remaining blocks are encrypted with previous ciphe bloc as the seed

- Cipher Feedback (CFB): a mode where data is being provided in a stream versus a block.
- Counter Feedback Mode (CTR): this mode is the combination of encrypting a counter which is then XOR’d with plain text.

## Cool links

[Cyberthreat map](https://cybermap.kaspersky.com/)
[Live Cyber threat map](https://threatmap.checkpoint.com/)

## Topics

- [[LOJAX]] attacks
- [[Multifernet]]
- [[Rotate]]
- [[Encryption]] - Asymmetric Encryption
- [[Digital signatures]]
- [[HMAC]]
- [[Bloom Filter]]
