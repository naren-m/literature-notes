- ``{{video https://www.youtube.com/watch?v=641_goNZGo`g}}`
-
- [Hired In Tech](https://www.hiredintech.com/system-design/)
- [System design Primer](https://github.com/naren-m/system-design-primer)
- [Code Karle Youtube - LeetCode used this](https://www.youtube.com/@codeKarle)
- {{video https://www.youtube.com/watch?v=ZaA0kNm18pE}}
- {{video https://www.youtube.com/watch?v=adOkTjIIDnk}}
-
- [Stop Reading Theory. These 18 Real Systems Explain 90% of Software Engineering](https://www.youtube.com/watch?v=7AQHB0lYaH8)
	- #[[Clip]] [(791) Stop Reading Theory. These 18 Real Systems Explain 90% of Software Engineering. - YouTube](https://www.youtube.com/watch?v=7AQHB0lYaH8)
	  The video, _Stop Reading Theory. These 18 Real Systems Explain 90% of Software Engineering_, by _Pascal Esc_, discusses the importance of learning software engineering by studying real-world systems rather than just theoretical concepts. The speaker emphasizes that while textbooks are valuable (1:35), understanding how these concepts are applied in real products is crucial for practical knowledge (1:40).
	  
	  The video highlights **18 real systems** that provide practical examples of software engineering principles (3:02):
	  
	  *   **Foundation Core Infrastructure:**
	      
	      *   **URL Shortener** (3:08): Teaches about hash functions, collision handling, and database indexing, especially at scale with distributed ID generation (3:52).
	      *   **Amazon S3** (4:15): Explains durability guarantees, data replication, checksums, and the evolution of eventual to strong read-after-write consistency (4:45).
	  *   **High Scale Systems (when millions become billions):**
	      
	      *   **YouTube and MySQL** (5:21): Demonstrates how relational databases can scale through aggressive sharding and extensive caching (5:35).
	      *   **Meta Serverless Functions** (6:25): Shows how to handle millions of serverless calls per second by pre-warming containers, using lightweight virtualization, and smart scheduling (6:31).
	  *   **Realtime and Messaging Architectures:**
	      
	      *   **Kafka's Design Philosophy** (7:43): Revolutionized messaging by retaining logs and enabling independent consumer offsets, supporting event-driven architectures (7:50).
	      *   **Slack Messaging Infrastructure** (8:22): Details real-time chat at scale using WebSocket connections, message persistence, presence detection, and channel-based sharding (8:24).
	  *   **Financial and Transactional Systems:**
	      
	      *   **Stripe's Idempotency** (9:23): Critical for preventing double charges in payment systems through unique request IDs (9:28).
	      *   **Stock Exchange Matching** (9:59): Requires low-latency design, lock-free algorithms, and performance optimization for high-frequency trading (10:27).
	  *   **Social and Content Platforms:**
	      
	      *   **Twitter's Timeline** (10:38): Explains the fan-out-on-write and fan-out-on-read hybrid approach for generating personalized timelines at scale (11:23).
	      *   **Reddit's Voting System** (11:43): Balances recency and popularity with caching layers and asynchronous vote count updates (11:48).
	      *   **Tinder's Geospatial Matching** (12:20): Involves geospatial indexing and querying for matching nearby users (12:23).
	  *   **Engineering at Massive Scale:**
	      
	      *   **Uber's Driver Matching** (13:02): Utilizes geospatial queries, predictive ETAs, and supply-demand balancing through geographic sharding (13:04).
	      *   **Google Docs Collaboration** (13:38): Achieves real-time collaborative editing using operational transformation to reconcile concurrent edits (13:40).
	  *   **Content Delivery and Media:**
	      
	      *   **Spotify's Music Streaming** (14:41): Employs aggressive predictive caching, CDNs, and peer-to-peer distribution for efficient music delivery (14:43).
	      *   **WhatsApp's Infrastructure** (15:09): Built on Erlang for lightweight processes and fault tolerance, prioritizing reliability through architectural simplicity (15:13).
	  *   **Platform Level Systems:**
	      
	      *   **AWS Scaling Strategies** (16:05): Emerged from Amazon's retail operations, focusing on treating servers as replaceable and using immutable infrastructure (16:09).
	      *   **ChatGPT's Architecture** (16:35): While proprietary, it likely involves model sharding, request batching, and extensive caching to handle unpredictable load spikes (16:39).
	  
	  By studying these real systems, engineers can recognize recurring patterns like **cache invalidation**, **sharding**, and **rate limiting**, which accelerate their growth and prepare them for interview questions (16:54).
- [](https://www.youtube.com/@pascal_esc)