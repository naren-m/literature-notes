---
layout: "default"
title: "Checksum"
word_count: 175
created: "2025-06-25T14:36:45.465195"
modified: "2025-06-25T14:36:45.465195"
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
  - title: "Docs"
    url: "/topics/docs//"
  - title: "Cse"
    url: "/topics/docs/cse//"
  - title: "Cryptography"
    url: "/topics/docs/cse/cryptography//"
  - title: "Checksum"
    url: "/topics/docs/cse/cryptography/checksum//"
---
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

Checksums are used to validate the [Integrity](cse/cryptography/integrity/) of the data.

[Hashing](cse/cryptography/hashing/) is different than Checksum.


LOST BITS
Lost of bits during some sort of transformation is a frequent scenario for employing checksums.
- Compressing / Decompression
- Network transmission
- File transfer
- Data transformation
Note that these use cases do not raise security issues. Nonetheless, [Integrity](cse/cryptography/integrity/) is still required.

MD5 should be enough.