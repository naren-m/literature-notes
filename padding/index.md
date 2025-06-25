---
layout: "default"
title: "Padding"
word_count: 66
created: "2024-11-28T18:24:53.185779"
modified: "2024-11-28T18:24:53.185779"
backlinks:
  - title: "Cryptography"
    url: "cse/cryptography/cryptography/"
  - title: "Cryptography"
    url: "logseq/bak/cse/cryptography/cryptography/2024-11-01t08_11_36626zdesktop/"
  - title: "Cryptography"
    url: "logseq/bak/cse/cryptography/cryptography/2024-11-29t01_57_40576zdesktop/"
---
# Padding

Encrypted data has a definitive start and end, based on the input. Hackers can potentially exploit this predictability. Yup, predictability again!
[Encryption](docs/cse/cryptography/encryption/index/) padding adds “random stuffing,” which further obfuscates the result. These are the two most popular padding schemes:
- OAEP (Optimal Asymmetric [Encryption](docs/cse/cryptography/encryption/index/) Padding)
- PKCS1 ([Public Key](docs/cse/cryptography/public-key/index/) [Cryptography](logseq/bak/cse/cryptography/cryptography/2024-11-29t01_57_40576zdesktop/) Standards)

The details of padding algorithms are beyond the scope of this course.
- https://bit.ly/3z6rMzq