---
title: "Transformers"
date: 2026-11-11
type: permanent
category: "Computer Science/Machine Learning"
tags: ["machine-learning", "deep-learning"]
status: draft
related: ["[[RNN]]", "[[LSTM]]"]
---
# Transformers

Neural network built on attention. "Attention Is All You Need", Vaswani et al., 2017.

- Self-attention: every token looks at every other token.
- No recurrence → the whole sequence is processed in parallel.
- [[RNN]], [[LSTM]] go step by step and struggle with long range.
- Base of today's LLMs.
- Cost: attention grows O(n²) with sequence length.
