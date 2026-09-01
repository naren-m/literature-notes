---
title: "DP Practice"
date: "2026-05-05"
type: "research"
category: "Legacy/Pages"
tags: ["dynamic-programming", "algorithms", "practice"]
status: "draft"
related: ["[[Dynamic Programming]]"]
---

# DP Practice

This note is a practice plan for [[Dynamic Programming]]. The goal is to learn how to model a problem as a set of states and transitions, then improve the implementation without changing the recurrence.

## Core method

1. Define the state in one sentence.
2. Write the transition from smaller states.
3. Identify the base cases.
4. Choose memoization or tabulation.
5. Check time and space complexity.
6. Test small inputs and boundary cases.

## Patterns to practice

- one-dimensional sequences and include/exclude decisions;
- grid and matrix paths;
- string matching and edit distance;
- interval and partition problems;
- knapsack and resource allocation;
- tree, state-machine, and bitmask problems.

## Practice loop

Start with a recursive solution so the recurrence is visible. Add memoization to remove repeated work. Convert to tabulation when the dependency order is clear. Then reduce memory only if the state transition allows it.

For each problem, write down the state, transition, base case, complexity, and one failed approach. Practice explaining those five items before looking at a solution.

## Resource

- [LeetCode Dynamic Programming study plan](https://leetcode.com/studyplan/dynamic-programming/)
