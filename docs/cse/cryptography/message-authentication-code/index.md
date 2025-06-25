---
layout: "default"
title: "Message Authentication Code (MAC)"
word_count: 48
created: "2024-11-28T18:24:53.168262"
modified: "2024-11-28T18:24:53.168262"
breadcrumbs:
  - title: "Home"
    url: "/"
  - title: "Cse"
    url: "/topics/cse//"
  - title: "Cryptography"
    url: "/topics/cse/cryptography//"
---
# Message Authentication Code (MAC)

A MAC verifies both the [Integrity](docs/cse/cryptography/integrity/index/) and Identification of a message.
The MAC consists of a keyed hash. This is a hash seeded with a *private key*
There are three aspects of a Mac:
- Creating a *private key*
- Signing a hash
- Verifying the MAC