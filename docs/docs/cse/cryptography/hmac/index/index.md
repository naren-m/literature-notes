---
layout: "default"
title: "HMAC"
word_count: 164
created: "2025-06-25T14:36:45.465562"
modified: "2025-06-25T14:36:45.465562"
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
  - title: "Cse"
    url: "/topics/docs/cse//"
  - title: "Cryptography"
    url: "/topics/docs/cse/cryptography//"
  - title: "Hmac"
    url: "/topics/docs/cse/cryptography/hmac//"
---
---
layout: "default"
title: "HMAC"
word_count: 100
created: "2024-11-28T18:24:53.167692"
modified: "2024-11-28T18:24:53.167692"
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
  - title: "Cse"
    url: "/topics/cse//"
  - title: "Cryptography"
    url: "/topics/cse/cryptography//"
---
# HMAC

HMAC is a hash that is seeded with a secret key. The two elements of HMAC.
• Hashing algorithm
• Authentication
HMAC can use a variety of hashing algorithms:

md5 --- sha1
sha224 --- sha256
sha384 --- black2b
black2s --- and others

Here is the implementation for HMAC in Python.
Call the hmac.new function to great new hashing used the password and the designated hashing algorithm.
hmac.new(plaintext, password, hashing algorithm)
import hashlib import hmac
hmac1 = hmac.new(b'info 1', b'1234', hashlib.md5)
hmac2 = hmac.new(b'info 2', b'1234', hashlib.sha1)
print("MD5", hmac1.hexdigest())
print("SHA1", hmac2.hexdigest())