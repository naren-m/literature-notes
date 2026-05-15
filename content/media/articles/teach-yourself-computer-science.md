---
title: "Teach Yourself Computer Science"
date: 2021-04-20
type: literature
category: "learning/cse"
tags: [computer-science, self-study, curriculum, bradfield, oz-nova]
status: want-to-study
source: "https://www.notion.so/085e8f6b53ea467c920d08dfce2f0fe8"
external: "https://teachyourselfcs.com/"
related: ["[[master-algorithms-and-data-structures]]", "[[sicp]]", "[[csapp]]", "[[classic-cs-problems-in-python]]", "[[designing-data-intensive-applications]]"]
---

# Teach Yourself Computer Science

Oz Nova & Myles Byrne's curated CS self-study guide (Bradfield School of CS). **The canonical starting roadmap for bootcamp grads / self-taught engineers** who want the foundations a CS degree would have given them — without doing a master's.

## Target audience

> We have in mind that you are a self-taught software engineer, bootcamp grad or precocious high school student, or a college student looking to supplement your formal education with some self-study.

Assumes some professional experience. "Students love learning about database systems if they have already worked with databases professionally."

## The 9 core subjects and their recommended resources

### 1. Programming fundamentals

- **SICP** — *Structure and Interpretation of Computer Programs* (Abelson & Sussman). "Just try it. Some people find SICP mind-blowing."
- Supplement with **How to Solve It** (Pólya) — general problem-solving; as applicable to CS as to math.

### 2. Computer architecture

- **CSAPP** — *Computer Systems: A Programmer's Perspective* (Bryant & O'Hallaron).

### 3. Algorithms and data structures

- **The Algorithm Design Manual** (Skiena).
- Alternatively **CLRS** for a more theoretical treatment (see [[intro-to-algorithms-clrs]]).

### 4. Math for CS

- **Discrete math** is the relevant branch (logic, combinatorics, probability, set theory, graph theory, cryptography-adjacent number theory).
- Start: László Lovász's lecture notes.
- Advanced: *Mathematics for Computer Science* (MIT 6.042 notes) — and [the MIT OCW video lectures](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/video-lectures/).
- **Linear algebra**: 3Blue1Brown's [Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) → Gilbert Strang (MIT 18.06).

> If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is. — John von Neumann

### 5. Operating systems

- Primary: **OSTEP** — *Operating Systems: Three Easy Pieces* (Remzi Arpaci-Dusseau), free online.
- Classic but criticized: Silberschatz's "Dinosaur book"; Tanenbaum's *Modern Operating Systems*.
- Hands-on: read and modify **xv6** (MIT port of Unix V6 to x86/ANSI C).

### 6. Computer networking

- Book: **Kurose & Ross**, *Computer Networking: A Top-Down Approach*. Do the Wireshark labs.
- Video: Stanford's *Introduction to Computer Networking* (YouTube unofficial playlists).

### 7. Databases

- The recommendation: **skip textbooks early**. Start with Joe Hellerstein's **CS 186** at Berkeley (YouTube).
- Key paper: [Architecture of a Database System](http://db.cs.berkeley.edu/papers/fntdb07-architecture.pdf) (Hellerstein, Stonebraker).
- Advanced: the **"Red Book"** — *Readings in Database Systems* (Bailis, Hellerstein, Stonebraker).
- Data modelling: *Data and Reality* by William Kent.

### 8. Languages and compilers

- Introductory: **Crafting Interpreters** (Bob Nystrom) — free online.
- Traditional: the **Dragon Book** (Aho/Sethi/Ullman); don't read cover-to-cover — cherry-pick.
- Video: Alex Aiken's Compilers course on edX.

> Don't be a boilerplate programmer. Instead, build tools for users and other programmers. Take historical note of textile and steel industries: do you want to build machines and tools, or do you want to operate those machines? — Ras Bodik

### 9. Distributed systems

- Primary: **DDIA** — *Designing Data-Intensive Applications* (Martin Kleppmann) — see [[designing-data-intensive-applications]].
- Alternative: van Steen & Tanenbaum, *Distributed Systems 3rd ed.* (free online).
- Video: **MIT 6.824** (Robert Morris) — papers + labs.
- Attend [Papers We Love](http://paperswelove.org/).

## Sequencing

- The subjects overlap cyclically; revisit throughout your career.
- Hard prerequisites:
  - **Computer architecture** before **operating systems / databases**.
  - **Networking + OS** before **distributed systems**.

## FAQ takeaways

- **AI / ML / graphics** are electives — not part of the core. Berkeley's AI course, Andrew Ng's Coursera ML, Berkeley CS 184 for graphics.
- **Language X?** Learning a language is easier and less valuable than learning *about* languages. After SICP + compilers, picking up a new language should take a weekend.
- **Trendy tech X?** Work backwards from the technology to the underlying concept.
- **Textbooks cheaply:** older editions are usually ~10x cheaper and 90%+ as good.

## How this maps into the vault

This roadmap informs [[master-algorithms-and-data-structures]] (the big Projects-DB checklist). The full TYCS pass is a multi-year project; breaking it into quarterly sub-projects per subject is likely realistic.

## Open threads

- Acquire SICP, CSAPP, and OSTEP as long-running research anchors.
- Cross-reference MIT 6.006 / 6.042 / 6.824 course notes in `content/research/courses/`.
- Pair with [[classic-cs-problems-in-python]] as a companion practice track.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/085e8f6b53ea467c920d08dfce2f0fe8). See [[notion-migration]].*
