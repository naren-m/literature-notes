---
title: "Token Authentication"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: ["security", "authentication"]
status: "draft"
related: ["[[Digital signatures]]", "[[Cryptography]]", "[[Authentication]]", "[[JSON]]", "[[Strong Authentication]]"]
---

# Token Authentication

Token represents the credentials of the user.

- Authenticate once → get a token → send it with later requests.
- Token signed with [[Digital signatures|digital signatures]] → service verifies origin and validity. Backed by [[Cryptography]].
- Mostly used in web services.
