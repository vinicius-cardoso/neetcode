# NeetCode 150

Working through the [NeetCode 150](https://neetcode.io/practice) to sharpen my
algorithm skills for technical interviews. One file per problem, each with my
reasoning, complexity analysis, and the wrong turn I took first.

## Layout

Directories are numbered in dependency order, following the NeetCode roadmap —
each topic assumes the intuition from the ones before it. Files are named
`<zero-padded LeetCode number>-<slug>.py`.

```
01-arrays-hashing/0217-contains-duplicate.py
```

## Running

Every file is self-verifying: the `__main__` block holds `assert` statements
covering the examples plus the empty and single-element edge cases. No test
framework, no dependencies.

```bash
python3 01-arrays-hashing/0217-contains-duplicate.py   # one problem
./run-all.sh                                           # everything
./run-all.sh 07-trees                                  # one topic
```

## Method

Not grinding every problem in a topic before moving on. Roughly 6–8 problems
per topic, then forward — interviews are mostly Medium, and spaced repetition
beats blocking. Second pass revisits earlier topics after the graph material.

Each solution gets a written **approach** paragraph before it counts as done.
If I can't explain why *this* data structure, I pattern-matched instead of
understanding.

## Progress

| # | Topic | Done | Last touched |
|---|-------|------|--------------|
| 01 | Arrays & Hashing | 1 | 2026-09-18 |
| 02 | Two Pointers | 0 | — |
| 03 | Stack | 0 | — |
| 04 | Binary Search | 0 | — |
| 05 | Sliding Window | 0 | — |
| 06 | Linked List | 0 | — |
| 07 | Trees | 0 | — |
| 08 | Tries | 0 | — |
| 09 | Backtracking | 0 | — |
| 10 | Heap / Priority Queue | 0 | — |
| 11 | Graphs | 0 | — |
| 12 | 1-D Dynamic Programming | 0 | — |
| 13 | 2-D Dynamic Programming | 0 | — |
| 14 | Intervals | 0 | — |
| 15 | Greedy | 0 | — |
| 16 | Advanced Graphs | 0 | — |
| 17 | Bit Manipulation | 0 | — |
| 18 | Math & Geometry | 0 | — |

**1 / 150 solved**
