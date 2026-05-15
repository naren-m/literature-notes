---
title: "Cisco Golang Course"
date: 2020-08-13
type: literature
category: "course/programming"
tags: [golang, go, concurrency, parallel, channels, csp, functional-programming, course-notes]
status: not-started
course: "Cisco Golang Course"
publisher: "Cisco Virtual"
field: CSE
topic: [Programming, "Programming Language"]
source: "https://www.notion.so/fc1c5cd7938344059d73b742fcdd3182"
related: []
---

# Cisco Golang Course — course notes

Cisco internal course on Go. Goal: learn Go's concurrency model (goroutines, channels, CSP) and its functional-programming constructs.

## Why I'm taking it

To learn about multi-threading and the functional paradigm of the Go language.

## Syllabus

- Parallel / threading concepts
- Communicating Sequential Processes (CSP)
- Channels
- Synchronization objects
- Functional programming theory
- Pure functions
- Currying
- Recursion
- Functors
- Continuation-passing style

## Parallel programming vs concurrency

**Concurrency.**
- Key differentiators:
  - Do multiple things; when blocked on one thing, do another. This is what most humans do.
  - It's all about *responsiveness*.
  - Multi-tasking.
  - Shared state.
- Related terms: Moore's Law, Amdahl's Law, embarrassingly parallel.

**Parallel programming.**
- Performance.
- Maximise utilisation of hardware.
- Scalability.

## Channels

*(Open: learn more about channels — the Notion page left a yellow highlight here.)*

## Traditional synchronisation primitives

- **WaitGroup** — most of what a semaphore can do can be done with `WaitGroup`; it is idiomatic in Go.
- **Mutex**
- **Cond**
- **RWLock**
- **Semaphore** — *no* semaphore type in Go's standard library.

## Language features

- No polymorphism in the classical sense — you use interfaces (this is called **duck typing**).
- Go uses **cooperative scheduling** on the logical processor. Each logical processor has a hard thread associated with it.
  - A goroutine runs over a thread.
  - Multiple goroutines run over the same thread.
- `main` is itself a goroutine.

### Cooperative scheduling

You won't be preempted for a CPU cycle; you voluntarily give up the CPU cycle.

### Threads

Every thread has a stack, and stacks are **expensive**. Each stack frame has parameters, locals, and function state. The stack grows continuously. The limitation on scalability is threads — threads consume more memory. **Goroutines are much lighter than threads.**

- The time slice for each thread is called a **quantum**; most OSes set it at 20 ms.
- Open questions: thread starvation? thread erosion?

## Open threads

- Flesh out channels — buffered vs unbuffered, select, directional channels, ownership patterns.
- Pair with [[resurrecting-duckling-model]] for the "duck typing" pun and with [[cisco-interviewer-training]] since this course was Cisco-internal.
- Functional-programming section is still stubbed; pull in references when the course is resumed (or pair with [[hashing]]-style research notes as the material accrues).

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/fc1c5cd7938344059d73b742fcdd3182). See [[notion-migration]] and [[courses-library]].*
