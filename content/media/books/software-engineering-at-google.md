---
title: "Software Engineering at Google: Lessons Learned from Programming Over Time"
date: 2022-02-08
type: literature
category: "software-engineering"
tags: [software-engineering, google, practices, testing, code-review, monorepo]
status: want-to-read
author: "Titus Winters, Tom Manshreck, Hyrum Wright"
source: "https://www.notion.so/dd5b716acf9a4838913cafa48cba4012"
external: "https://www.oreilly.com/library/view/software-engineering-at/9781492082781/"
related: ["[[designing-data-intensive-applications]]", "[[teach-yourself-computer-science]]"]
---

# Software Engineering at Google

Winters, Manshreck & Wright's *Software Engineering at Google* (O'Reilly, 2020) — a look at how one of the largest engineering organisations in the world (50k+ engineers, ~2 billion LOC monorepo) organises itself to build software that keeps working over years and decades.

## Thesis from the preface

> "Software engineering" implies the application of theoretical knowledge to build something real and precise. Aeronautical engineers must follow rigid guidelines and practices, because errors in their calculations can cause real damage; programming, on the whole, has traditionally not followed such rigorous practices. But, as software becomes more integrated into our lives, we must adopt and rely on more rigorous engineering methods.

Key reframing: **software engineering is programming integrated over time**. The longer a codebase lives, the more its engineering (vs. programming) practices dominate.

## What the book does *not* cover

Explicitly out of scope (each would be its own book):

- Software design (broad architectural design)
- Project management
- API design
- Security hardening
- Internationalization
- UI / frontend frameworks
- Language-specific concerns

The book is language-neutral by design.

## Core topics covered (table of contents)

- **Culture**: software engineering vs. programming, team culture, knowledge sharing, leadership.
- **Processes**: style guides, code review, documentation, testing (Small/Medium/Large), deprecation.
- **Tools**: version control at scale (Piper/Git, monorepo vs. polyrepo), build systems (Blaze/Bazel), CI at scale, code search, static analysis.
- **Specific practices**: trunk-based development, Beyoncé Rule ("If you liked it, you shoulda put a CI test on it"), Hyrum's Law ("with a sufficient number of users of an API, every observable behaviour will be depended upon by somebody").

## Hyrum's Law (one of the book's most cited contributions)

> With a sufficient number of users of an API, it does not matter what you promise in the contract: all observable behaviours of your system will be depended on by somebody.

Changes things you didn't think were part of the contract — timing, ordering, error messages — *will* break downstream users.

## How this fits the vault

Complements [[designing-data-intensive-applications]] — DDIA covers systems, this covers *engineering process at scale*. Useful companion to any "senior engineer leveling up" track.

## Open threads

- Extract the Beyoncé Rule, Hyrum's Law, and the "size of tests" pyramid as standalone research notes.
- Pair with *The Pragmatic Programmer* as an individual-practitioner counterpart to the organizational focus here.
- Free to read: Google hosts the book online at [abseil.io/resources/swe-book](https://abseil.io/resources/swe-book).

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/dd5b716acf9a4838913cafa48cba4012). See [[notion-migration]].*
