---
title: "systemdesign inbox"
date: "2026-05-05"
type: "research"
category: "Legacy/Pages"
tags: ["system-design", "inbox"]
status: "draft"
---

# systemdesign inbox

- ``{{video https://www.youtube.com/watch?v=641_goNZGo`g}}`

- [Hired In Tech](https://www.hiredintech.com/system-design/)
- [System design Primer](https://github.com/naren-m/system-design-primer)
- [Code Karle Youtube - LeetCode used this](https://www.youtube.com/@codeKarle)
- {{video https://www.youtube.com/watch?v=ZaA0kNm18pE}}
- {{video https://www.youtube.com/watch?v=adOkTjIIDnk}}

- [Stop Reading Theory. These 18 Real Systems Explain 90% of Software Engineering](https://www.youtube.com/watch?v=7AQHB0lYaH8)
  - Clip [(791) Stop Reading Theory. These 18 Real Systems Explain 90% of Software Engineering. - YouTube](https://www.youtube.com/watch?v=7AQHB0lYaH8)
    By _Pascal Esc_. Stop reading only theory. Textbooks are fine (1:35); seeing the concept inside a real product is what sticks (1:40).

    **18 real systems** (3:02):

    - **Foundation Core Infrastructure:**

        - **URL Shortener** (3:08): hash functions, collisions, DB indexing; distributed ID generation at scale (3:52).
        - **Amazon S3** (4:15): durability, replication, checksums; eventual → strong read-after-write consistency (4:45).
    - **High Scale Systems (when millions become billions):**

        - **YouTube and MySQL** (5:21): relational DB scales fine with aggressive sharding + caching (5:35).
        - **Meta Serverless Functions** (6:25): millions of calls/sec → pre-warmed containers, lightweight virtualization, smart scheduling (6:31).
    - **Realtime and Messaging Architectures:**

        - **Kafka's Design Philosophy** (7:43): keep the log, let each consumer own its offset → event-driven architectures (7:50).
        - **Slack Messaging Infrastructure** (8:22): WebSockets, message persistence, presence, channel-based sharding (8:24).
    - **Financial and Transactional Systems:**

        - **Stripe's Idempotency** (9:23): unique request IDs → no double charges (9:28).
        - **Stock Exchange Matching** (9:59): low latency, lock-free algorithms, HFT-grade performance (10:27).
    - **Social and Content Platforms:**

        - **Twitter's Timeline** (10:38): hybrid fan-out-on-write + fan-out-on-read (11:23).
        - **Reddit's Voting System** (11:43): recency vs popularity; caching + async vote counts (11:48).
        - **Tinder's Geospatial Matching** (12:20): geospatial indexing to match nearby users (12:23).
    - **Engineering at Massive Scale:**

        - **Uber's Driver Matching** (13:02): geospatial queries, predictive ETAs, supply-demand balancing via geographic sharding (13:04).
        - **Google Docs Collaboration** (13:38): operational transformation reconciles concurrent edits (13:40).
    - **Content Delivery and Media:**

        - **Spotify's Music Streaming** (14:41): predictive caching, CDNs, peer-to-peer (14:43).
        - **WhatsApp's Infrastructure** (15:09): Erlang: lightweight processes, fault tolerance. Reliable because simple (15:13).
    - **Platform Level Systems:**

        - **AWS Scaling Strategies** (16:05): came out of Amazon retail. Servers are replaceable; immutable infrastructure (16:09).
        - **ChatGPT's Architecture** (16:35): proprietary; likely model sharding, request batching, caching for load spikes (16:39).

    Same patterns keep coming back: **cache invalidation**, **sharding**, **rate limiting** (16:54).
- [](https://www.youtube.com/@pascal_esc)
