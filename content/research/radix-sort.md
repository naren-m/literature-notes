---
title: "Radix sort"
date: 2020-09-14
type: research
category: "CSE/algorithms"
tags: [algorithms, sorting, radix-sort, non-comparison-sort]
status: incomplete
source: "Notion Notes DB, course notes"
related: [sorting, counting-sort]
---

# Radix sort

Short research note on radix sort. Builds on [[counting-sort]] to sort fixed-width integer keys in linear time.

## Idea

Use each digit of the key as a sort key, running a stable subsort (usually [[counting-sort]]) once per digit. Because the subsort is stable, the final pass leaves all digits in the correct order.

Two conventions exist:

- **LSD (least-significant-digit first)** — start with the rightmost digit and work leftward. Stability of the subsort is what makes this correct.
- **MSD (most-significant-digit first)** — start with the leftmost digit, recursing into buckets of equal leading digit. Useful for variable-length keys (e.g., strings).

The Notion note mentions both directions; LSD is the form that "magically" sorts at the end, because repeated stable sorts by less-significant keys preserve the order established by more-significant keys.

## Complexity

- Time: `Θ(d · (n + b))` where `d` = number of digits and `b` = base (alphabet size).
- For `b = O(n)` and `d = O(1)`: linear time.

## Open threads

- Reconcile the contradiction in the original capture (which says both "start with LSD" and "start with MSD"). LSD is the classic choice here.
- Worked example on small integer array.
- Connection to bucket sort.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/05f74ac7a4ee4979b952c622726a7915). See [[notion-migration]].*
