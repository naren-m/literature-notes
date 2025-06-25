---
layout: "default"
title: "Digital signatures"
word_count: 289
created: "2025-06-25T14:36:45.467778"
modified: "2025-06-25T14:36:45.467778"
backlinks:
  - title: "Cryptography"
    url: "cse/cryptography/cryptography/"
  - title: "Encryption"
    url: "cse/cryptography/encryption/"
  - title: "Fingerprint"
    url: "cse/cryptography/fingerprint/"
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
  - title: "Digital Signatures"
    url: "/topics/docs/cse/cryptography/digital-signatures//"
---
---
layout: "default"
title: "Digital signatures"
word_count: 198
created: "2024-11-28T18:24:53.167356"
modified: "2024-11-28T18:24:53.167356"
backlinks:
  - title: "Cryptography"
    url: "cse/cryptography/cryptography/"
  - title: "Encryption"
    url: "cse/cryptography/encryption/"
  - title: "Fingerprint"
    url: "cse/cryptography/fingerprint/"
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
# Digital signatures

Digital Signature = [Hashing](cse/cryptography/hashing/) + [Encryption](cse/cryptography/encryption/) (encrypted with Private key and decrypted by Public key)
- Use asymmetric encryption.
- Sender creates a digital signature while the receiver verifies the signature.
- Does NOT provide Confidentiality

Digital signatures are a combination of hashing and encryption to verify the identity of a sender and integrity of the message.

Digital signatures potentially defend against several vulnerabilities in [STRIDE](logseq/bak/cse/cryptography/stride/2024-11-29t01_57_40582zdesktop/):
- Spoofing
- Tampering
- Repudiation

Digital signatures are a combination of hashing and encryption. This potentially resolves several vulnerabilities identified within STRIDE:
- Spoofing
- Tampering
- Information disclosure*
- Repudiation


## Sender

Digital signatures are useful for sending data securely with identity. It is a combination of a hash and asymmetric encryption.
Here are the steps to create a digital signature for a message / data:
1. Create a hash of the message
2. Encrypt the hash with the private key. The result is a digital signature.
3. Send the digital signature to the receiver with the message


## Receiver

The recipient receives the signature and plaintext. Before using the plaintext, verify the signature.
1. Hash (hash 1) the plaintext
2. Decrypt the signature and extricate the hash (hash 2)
3. Compare the two hashes. If the same, the signature has been verified.