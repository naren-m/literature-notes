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

- Plan for [[Dynamic Programming]]: [LeetCode DP study plan](https://leetcode.com/studyplan/dynamic-programming/)
- Video: [Abdul Bari](https://www.youtube.com/watch?v=5dRGRueKU3M)

## Every problem, same steps
- Is it DP? Overlapping subproblems? Optimizing min/max/count?
- State in one sentence. What does `dp[i]` / `dp[i][j]` mean?
- Recurrence from smaller states. Base cases.
- Recursive → memoized → tabulated. Then squeeze space (rolling array, few variables).
- Edge cases. Time and space.
- Draw the recursion tree for small inputs when stuck.

## Common mistakes
- State not clearly defined.
- Forgot base cases.
- Off-by-one.
- Missed a transition.
- State too complicated.

## Phases
| Phase | Weeks | Start | Focus | Problems (LC) |
|---|---|---|---|---|
| 1 | 1-2 | Aug 4th, 2025 | Fibonacci-style, 30 min/day | 70, 746, 198 |
| 2 | 3-4 | Aug 18th, 2025 | 1D linear + include/exclude | 213, 53, 152, 300, 139, 416, 494 |
| 3 | 5-6 | Sep 1st, 2025 | Grid, string, interval | 62, 63, 64, 221, 1143, 72, 115, 10, 516, 647 |
| 4 | 7-8 | Sep 15th, 2025 | Knapsack, state machine, tree | 322, 518, 377, 309, 714, 256, 337, 124 |
| 5 | 9-10 | Sep 29th, 2025 | Complex state, bitmask | 312, 1547, 877, 1140, 1406, 847 |

## Problem list by pattern (LC numbers)
| Pattern | Problems |
|---|---|
| 1D / linear | 70, 746, 509, 338, 392, 198, 213, 53, 152, 918, 91, 55, 45, 1306, 322, 518, 279, 413, 647, 650 |
| 2D grid | 62, 63, 64, 221, 1277, 931, 1314, 688, 576; hard: 980, 174, 1289, 85, 329, 1463 |
| String | 5, 516, 1143, 583, 712, 97, 1035; hard: 72, 115, 940, 44, 10, 87, 132, 1092, 1312 |
| Tree | 543, 337, 1372, 1339; hard: 124, 968, 1373, 2246 |
| Interval | 1039, 647; hard: 312, 1000, 1547, 664, 1771 |
| 0/1 knapsack | 416, 494, 1049, 474 |
| Unbounded knapsack | 322, 518, 377 |
| Advanced knapsack | 879, 1449, 956 |
| State machine (stocks) | 121, 122, 123, 188, 309, 714 |
| Bitmask | 698, 847, 943, 1125, 1494, 1879, 1986 |
| Game theory | 486, 877, 1140, 464, 375; hard: 1406, 1563, 913 |

- Beginner order: 70, 509, 746 → 53, 198, 121 → 62, 64 → 5, 1143.
