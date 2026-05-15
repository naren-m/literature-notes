---
title: "Solve interval-based problems"
date: 2022-07-10
type: literature
category: "CSE/algorithms"
tags: [algorithms, intervals, leetcode, programming-practice]
status: complete
source: "https://medium.com/interviewnoodle/leetcode-5-tricks-to-solve-any-interval-conflict-schedule-related-problems-3f33d6e5af55"
related: []
---

# Solve interval-based problems

Literature note for a Medium article on tricks for merge / insert / intersect interval problems. Captures the article's structure and the techniques it advocates.

## Why interval problems matter

Intervals represent either a period of time or a range of numbers. They are the key element in scheduling problems: restaurant reservations without conflicts, CPU resource scheduling, assigning classes to teachers. Many Leetcode problems involve interval operations.

## 1. Understand the basic interval relations

For two intervals A and B there are only three possible relations:

- No overlap
- Completely overlap
- Partially overlap

## 2. Sort the intervals first

If input is not sorted, sort by **start** time in non-decreasing order before doing anything else.

```
intervals.sort(); // Sort by start time first => O(n log n)
```

## 3. Merge operation

Non-overlapping intervals have nothing to merge. For overlap, two intervals A and B overlap when B starts before A finishes.

```
if (b.start <= a.end) {
    mergedIntervalEnd = Math.max(a.end, b.end);
}
```

## 4. Intersect operation

Non-overlapping intervals have no intersection. For overlapping intervals, the intersection exists when the latest start is less than or equal to the earliest end.

```
if (Math.max(a.start, b.start) <= Math.min(a.end, b.end)) {
    intersect = [Math.max(a.start, b.start), Math.min(a.end, b.end)];
}
```

## 5. Practice problems from the article

### Merge Intervals (Leetcode)

Given an array of intervals, merge all overlapping intervals.

1. Input isn't sorted — sort by start time first. `O(n log n)`.
2. Scan once checking for overlap with previous. `O(n)`.
3. Merge based on overlap check.

Overall: `O(n log n)` time, `O(n)` space. The sort is the bottleneck.

### Insert Interval (Leetcode)

Input is already sorted, and a new interval must be inserted while preserving non-overlap.

1. No sort needed — input is pre-sorted.
2. Find the first interval whose end is greater than or equal to the new interval's start; insert there; merge any subsequent overlaps.

Overall: `O(n)` time, `O(n)` space.

### Interval List Intersections (Leetcode)

Given two lists of pairwise-disjoint, sorted intervals, return their intersections.

1. No sort needed.
2. Walk both lists using the trick 4 intersection check.

Overall: `O(M + N)` time and space.

## Takeaways

- Sorting by start is the default opening move for interval problems unless the input is pre-sorted.
- Overlap and intersection are small, memorizable predicates — they are the core primitives.
- Recognize `[start, end]` pair problems as the "interval family" and reach for these primitives first.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/c4e4688a2e8949bcbbde41ac512018b2). See [[notion-migration]].*
