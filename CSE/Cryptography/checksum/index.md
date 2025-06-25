---
layout: "default"
title: "Checksum"
word_count: 96
created: "2024-11-28T18:24:53.149941"
modified: "2024-11-28T18:24:53.149941"
backlinks:
  - title: "Cryptography"
    url: "cse/cryptography/cryptography/"
  - title: "Hashing"
    url: "cse/cryptography/hashing/"
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
# Checksum

Checksums are created to provide data integrity but are considered lightweight hashes. Not every target of hashing requires a security-level hash, such as SHA-256.
Checksums are a highly performant and insecure hash.

Checksum -> Integrity

Checksums are used to validate the [Integrity](docs/cse/cryptography/integrity/index/) of the data.

[Hashing](docs/cse/cryptography/hashing/index/) is different than Checksum.


LOST BITS
Lost of bits during some sort of transformation is a frequent scenario for employing checksums.
- Compressing / Decompression
- Network transmission
- File transfer
- Data transformation
Note that these use cases do not raise security issues. Nonetheless, [Integrity](docs/cse/cryptography/integrity/index/) is still required.

MD5 should be enough.