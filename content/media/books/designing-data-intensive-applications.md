---
title: "Designing Data-Intensive Applications (DDIA)"
date: 2022-02-08
type: literature
category: "software-engineering/distributed-systems"
tags: [ddia, distributed-systems, databases, storage, consensus, kleppmann]
status: want-to-read
author: "Martin Kleppmann"
source: "https://www.notion.so/b03df36d9e884808b7926396a097b24a"
external: "https://dataintensive.net/"
related: ["[[teach-yourself-computer-science]]", "[[understanding-distributed-systems]]", "[[software-engineering-at-google]]"]
---

# Designing Data-Intensive Applications

Martin Kleppmann's *Designing Data-Intensive Applications* (O'Reilly, 2017) — universally "DDIA". The canonical modern textbook on building systems that are **reliable, scalable, and maintainable** at scale.

## Stance (from Kleppmann's preface)

> The term 'Big Data' is so overused and underdefined that it is not useful in a serious engineering discussion. This book uses less ambiguous terms, such as single-node versus distributed systems, or online/interactive versus offline/batch processing systems.

Bias toward **FOSS**: reading, modifying, and running source is how you understand a system. Vendor lock-in is a risk worth spending engineering cycles to avoid.

## Structure (three parts)

1. **Foundations of data systems** — reliability / scalability / maintainability; data models (relational / document / graph); storage & retrieval (B-trees, LSM-trees, column stores); encoding (Protobuf, Avro, Thrift) and evolution.
2. **Distributed data** — replication (leader/follower, multi-leader, leaderless), partitioning (hash-based, range-based, secondary indexes), transactions (isolation levels, serializability, SSI), the trouble with distributed systems (unreliable networks, clocks, processes), consistency & consensus (linearizability, CAP, total-order broadcast, Raft/Paxos).
3. **Derived data** — batch processing (MapReduce, Spark), stream processing (Kafka, exactly-once), and the future of data systems (unbundling the database, end-to-end arguments).

## Why DDIA is the recommended text

- Practitioner-first: built for engineers working on real systems, not for graduate theorists.
- Rigorous and honest about trade-offs (CAP/PACELC, FLP, replication lag, read-after-write).
- Extensive citations → serves as a launchpad into the primary-literature papers.
- Covers the architecture of a database system at a level most textbooks don't — locks, logs, snapshot isolation.

## How this fits the vault

Kleppmann is the *Teach Yourself CS* recommended text for distributed systems (see [[teach-yourself-computer-science]] §9). This is the anchor book for any [[master-algorithms-and-data-structures]] systems-design track.

## Open threads

- Kleppmann's blog + talks (his "Please stop calling databases CP or AP" piece).
- The second edition (expected) will include CRDTs and local-first software.
- Pair with Vitillo's [[understanding-distributed-systems]] as a more-introductory companion.
- Pair with the MIT 6.824 reading list from [[teach-yourself-computer-science]].

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/b03df36d9e884808b7926396a097b24a). See [[notion-migration]].*
