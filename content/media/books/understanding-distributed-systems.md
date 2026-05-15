---
title: "Understanding Distributed Systems"
date: 2022-02-08
type: literature
category: "software-engineering/distributed-systems"
tags: [distributed-systems, vitillo, consensus, resiliency, observability]
status: want-to-read
author: "Roberto Vitillo"
source: "https://www.notion.so/bb61097f08904fa0b9ea962e8a7030c6"
external: "https://www.amazon.com/Understanding-Distributed-Systems-applications/dp/1838430202"
related: ["[[designing-data-intensive-applications]]", "[[software-engineering-at-google]]", "[[teach-yourself-computer-science]]"]
---

# Understanding Distributed Systems

Roberto Vitillo's *Understanding Distributed Systems: What every developer should know about large distributed applications*. A pragmatic, practitioner-oriented intro book designed to sit *between* academic papers (too theoretical) and engineering blog posts (too narrow).

## Stance

> Learning to build distributed systems is hard, especially if they are large scale. It's not that there is a lack of information out there… The problem is that the available information is spread out all over the place, and if you were to put it on a spectrum from theory to practice, you would find a lot of material at the two ends, but not much in the middle.
>
> That is why I decided to write a book to teach the fundamentals of distributed systems so that you don't have to spend countless hours scratching your head to understand how everything fits together. **This is the guide I wished existed when I first started out.**

Explicit audience: back-end web/mobile engineers.

## Table of contents

### 1. Introduction
1.1 Communication · 1.2 Coordination · 1.3 Scalability · 1.4 Resiliency · 1.5 Operations · 1.6 Anatomy of a distributed system.

### Part I — Communication
- **2 Reliable links** — reliability, connection lifecycle, flow control, congestion control, custom protocols.
- **3 Secure links** — encryption, authentication, integrity, handshake.
- **4 Discovery.**
- **5 APIs** — HTTP, resources, request methods, response status codes, OpenAPI, evolution.

### Part II — Coordination
- **6 System models.**
- **7 Failure detection.**
- **8 Time** — physical clocks, logical clocks, vector clocks.
- **9 Leader election** — Raft leader election, practical considerations.
- **10 Replication** — state machine replication, consensus, consistency models, chain replication, solving CAP, coordination avoidance.
- **11 Transactions** — ACID, isolation, atomicity, asynchronous transactions.

### Part III — Scalability
- **12 Functional decomposition** — microservices, API gateway, CQRS, messaging.
- **13 Partitioning** — sharding strategies, rebalancing.
- **14 Duplication** — network load balancing, replication, caching.

### Part IV — Resiliency
- **15 Common failure causes** — single point of failure, unreliable network, slow processes, unexpected load, cascading failures, risk management.
- **16 Downstream resiliency** — timeout, retry, circuit breaker.
- **17 Upstream resiliency** — load shedding, load leveling, rate-limiting, bulkhead, health endpoint, watchdog.

### Part V — Testing and operations
- **18 Testing** — scope, size, practical considerations.
- **19 Continuous delivery and deployment** — review/build, pre-production, production, rollbacks.
- **20 Monitoring** — metrics, SLIs, SLOs, alerts, dashboards, on-call.
- **21 Observability** — logs, traces, putting it all together.
- **22 Final words.**

## How this fits the vault

Vitillo is the **intro course**; Kleppmann's [[designing-data-intensive-applications]] is the **standard reference**. Read Vitillo first if coming from a web-app background; read DDIA for depth.

## Open threads

- Pull up each of the resiliency patterns (timeout / retry / CB / bulkhead / shed / level / rate-limit) as individual research notes.
- Cross-link to [[software-engineering-at-google]] for the practice-of-engineering counterpart.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/bb61097f08904fa0b9ea962e8a7030c6). See [[notion-migration]].*
