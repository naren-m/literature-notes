---
layout: "default"
title: "Message Authentication Code (MAC)"
word_count: 89
created: "2025-06-25T14:36:45.431913"
modified: "2025-06-25T14:36:45.431913"
breadcrumbs:
  - title: "Home"
    url: "/"
  - title: "Docs"
    url: "/topics/docs//"
  - title: "Cse"
    url: "/topics/docs/cse//"
  - title: "Cryptography"
    url: "/topics/docs/cse/cryptography//"
  - title: "Message Authentication Code"
    url: "/topics/docs/cse/cryptography/message-authentication-code//"
---
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

A MAC verifies both the [Integrity](cse/cryptography/integrity/) and Identification of a message.
The MAC consists of a keyed hash. This is a hash seeded with a *private key*
There are three aspects of a Mac:
- Creating a *private key*
- Signing a hash
- Verifying the MAC