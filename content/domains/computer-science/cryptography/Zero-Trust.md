---
title: "Zero-Trust"
date: "2026-04-30"
type: "permanent"
category: "Computer Science/Security"
tags: ["security", "authentication", "architecture"]
status: "draft"
source: "https://www.paloaltonetworks.com/cyberpedia/what-is-a-zero-trust-architecture"
related: ["[[Authentication]]", "[[Strong Authentication]]", "[[Data Sensitivity]]", "[[LOJAX]]", "[[Root of trust]]"]
---

# Zero-Trust

Philosophy: "never trust, always verify".

My definition:
- Security by eliminating implicit trust (based on firewalls, iptables etc.).
- Uses [[Strong Authentication]] to verify the workloads.

How it works:
- Old way: verify identity once at the perimeter, trust everything inside.
- Zero trust: "microperimeters" around specific assets (data, apps, services), each with its own [[Authentication]].
- Auth = identity + device, location, timestamp, recent activity, the request itself. Can run passively in the background.
- Approved users get only the privileges they need right now → attacker gets in, can't move freely.

Why:
- Attackers piggyback on approved users' access, then move laterally.
- Data, apps, users spread across cloud, hybrid, many locations → no defensible perimeter left.
- Layered point solutions leave gaps.

Not a product. An architecture discipline. Handle [[Data Sensitivity]] carefully.

## Reference

<https://www.cisco.com/c/en/us/solutions/automation/what-is-zero-trust-networking.html>
<https://www.paloaltonetworks.com/cyberpedia/what-is-a-zero-trust-architecture>
