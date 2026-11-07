---
title: "Testing Pyramid"
date: "2026-04-30"
type: "permanent"
category: "Computer Science/Coding Practices"
tags: ["testing", "software-engineering"]
status: "draft"
source: "http://www.agilenutshell.com/episodes/41-testing-pyramid"
related: ["[[Testing Principles]]", "[[Test Driven Dev]]", "[[Maintaining code base]]"]
---

# Testing Pyramid

![Testing pyramid: many unit tests at the base, fewer integration tests, fewest end-to-end tests at the top](https://raw.githubusercontent.com/naren-m/literature-notes/main/content/domains/computer-science/coding-practices/assets/testing-pyramid.svg)

Simple idea. Balance your automated tests by cost and how fast they give you feedback.

## The three layers

**Unit tests at the base. Lots of them.** They test one small piece in isolation. Fast. Run them all the time.

**Integration tests in the middle. Fewer.** They check that components talk to each other correctly. More setup, harder to debug.

**End-to-end tests at the top. Fewest.** They run the real workflow. That is the confidence you want, but they are slow, brittle, and when one fails you go digging.

## Here is the thing

Higher-level tests still matter. But an expensive test should only prove what a cheaper test can't. If you repeat the same assertion at every layer, you get a slow suite and almost no extra confidence.

Think of it as the cost of a bug. Catch it in a unit test, it's tiny. In an integration test, you're on a call with another team. In an end-to-end test, it eats your afternoon. Club all the layers into one giant test and the pyramid flips over and melts. Nobody knows what failed.

![Comic: a bug caught in a unit test is tiny and cheap, in an integration test it needs a team call, in an end-to-end test it eats the afternoon; clubbing all layers into one giant test makes a melting upside-down pyramid where nobody knows what failed](https://raw.githubusercontent.com/naren-m/literature-notes/main/content/domains/computer-science/coding-practices/assets/testing-pyramid-bug-cost.svg)

- [[Testing Principles]]
- [[Test Driven Dev]]
- [[Maintaining code base]]
