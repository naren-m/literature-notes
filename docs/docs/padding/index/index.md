---
layout: "default"
title: "Padding"
word_count: 133
created: "2025-06-25T14:36:45.465321"
modified: "2025-06-25T14:36:45.465321"
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
  - title: "Docs"
    url: "/topics/docs//"
  - title: "Padding"
    url: "/topics/docs/padding//"
---
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
[Encryption](cse/cryptography/encryption/) padding adds “random stuffing,” which further obfuscates the result. These are the two most popular padding schemes:
- OAEP (Optimal Asymmetric [Encryption](cse/cryptography/encryption/) Padding)
- PKCS1 ([Public Key](cse/cryptography/public-key/) [Cryptography](logseq/bak/cse/cryptography/cryptography/2024-11-29t01_57_40576zdesktop/) Standards)

The details of padding algorithms are beyond the scope of this course.
- https://bit.ly/3z6rMzq