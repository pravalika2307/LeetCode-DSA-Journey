# LeetCode DSA Journey

A structured, recruiter-friendly repository documenting my Data Structures and Algorithms (DSA) learning journey in **Python** from **May 2026 to November 2026**.

---

## Introduction

Between May 2026 and November 2026, I practised LeetCode problems across core DSA patterns and consolidated **218 unique problems** into clean, optimal Python solutions following the official LeetCode `class Solution` format, backed by an automated `unittest` suite in [`tests/`](tests/).

- **Author:** Pravalika ([github.com/pravalika2307](https://github.com/pravalika2307))
- **Language:** Python 3
- **Learning Period:** May 2026 – November 2026

---

## Learning Timeline

A retrospective month-by-month breakdown is maintained in [`Progress/learning_timeline.md`](Progress/learning_timeline.md):

| Period | Primary Topic Focus | Problems Documented | Status |
| :--- | :--- | :---: | :--- |
| **May 2026 – June 2026** | Arrays & Matrix Traversal | 55 | Covered |
| **July 2026** | Hashing & Frequency Maps | 40 | Covered |
| **August 2026** | Two Pointers | 30 | Covered |
| **September 2026** | Sliding Window | 33 | Covered |
| **October 2026** | Binary Search & Search on Answer | 36 | Covered |
| **November 2026** | Linked Lists & Final Review | 24 | Covered |
| **Dec 2026 onward** | Strings, Stack/Queue, Trees, Heap, Backtracking, Graphs, DP, Greedy | 0 | Upcoming |

---

## Progress Dashboard

All counts below are verified directly against the solution files in this repository.

### Overall Progress

- **Total Unique Problems Documented:** `218`
- **Easy:** `84` (38.5%)
- **Medium:** `112` (51.4%)
- **Hard:** `22` (10.1%)

### Topic-Wise Distribution

| Folder | Topic | Total | Easy | Medium | Hard | Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| [`01_Arrays/`](01_Arrays/) | Arrays & Matrix | 55 | 28 | 22 | 5 | Covered |
| [`03_Hashing/`](03_Hashing/) | Hashing | 40 | 22 | 16 | 2 | Covered |
| [`04_Two_Pointers/`](04_Two_Pointers/) | Two Pointers | 30 | 11 | 17 | 2 | Covered |
| [`05_Sliding_Window/`](05_Sliding_Window/) | Sliding Window | 33 | 3 | 23 | 7 | Covered |
| [`06_Binary_Search/`](06_Binary_Search/) | Binary Search | 36 | 11 | 21 | 4 | Covered |
| [`07_Linked_List/`](07_Linked_List/) | Linked List | 24 | 9 | 13 | 2 | Covered |
| [`02_Strings/`](02_Strings/) | Strings (Dedicated Algorithms) | 0 | 0 | 0 | 0 | Upcoming |
| [`08_Stack_Queue/`](08_Stack_Queue/) | Stack & Queue | 0 | 0 | 0 | 0 | Upcoming |
| [`09_Trees/`](09_Trees/) | Trees & Tries | 0 | 0 | 0 | 0 | Upcoming |
| [`10_Heap/`](10_Heap/) | Heap / Priority Queue | 0 | 0 | 0 | 0 | Upcoming |
| [`11_Backtracking/`](11_Backtracking/) | Backtracking | 0 | 0 | 0 | 0 | Upcoming |
| [`12_Graphs/`](12_Graphs/) | Graphs | 0 | 0 | 0 | 0 | Upcoming |
| [`13_Dynamic_Programming/`](13_Dynamic_Programming/) | Dynamic Programming | 0 | 0 | 0 | 0 | Upcoming |
| [`14_Greedy/`](14_Greedy/) | Greedy | 0 | 0 | 0 | 0 | Upcoming |
| **Total** | **All Topics** | **218** | **84** | **112** | **22** | **6 Covered / 8 Upcoming** |

### Pattern-Wise Distribution

| Pattern Family | Count | Easy | Medium | Hard |
| :--- | :---: | :---: | :---: | :---: |
| Two Pointers & Cycle Detection | 43 | 20 | 21 | 2 |
| Hashing & Frequency Maps | 41 | 23 | 16 | 2 |
| Binary Search | 36 | 11 | 21 | 4 |
| Sliding Window | 33 | 3 | 23 | 7 |
| Linked List Pointer Manipulation | 18 | 5 | 11 | 2 |
| Greedy, Kadane & Voting | 12 | 4 | 6 | 2 |
| Matrix Traversal & In-Place Ops | 10 | 3 | 7 | 0 |
| Array Scanning, Reversal & Math | 8 | 6 | 2 | 0 |
| Cyclic Placement / Marking | 4 | 2 | 1 | 1 |
| Prefix / Suffix Computations | 4 | 3 | 1 | 0 |
| Dynamic Programming Basics | 3 | 2 | 1 | 0 |
| Bit Manipulation (XOR) | 2 | 2 | 0 | 0 |
| Divide and Conquer / Merge Sort | 2 | 0 | 0 | 2 |
| Sorting & Interval Merging | 2 | 0 | 2 | 0 |
| **Total** | **218** | **84** | **112** | **22** |

See [`Progress/pattern_tracker.md`](Progress/pattern_tracker.md) for the full problem-to-pattern mapping.

---

## Topics Covered

1. **Arrays & Matrix** ([`01_Arrays/`](01_Arrays/)) — 55 problems
2. **Hashing** ([`03_Hashing/`](03_Hashing/)) — 40 problems
3. **Two Pointers** ([`04_Two_Pointers/`](04_Two_Pointers/)) — 30 problems
4. **Sliding Window** ([`05_Sliding_Window/`](05_Sliding_Window/)) — 33 problems
5. **Binary Search** ([`06_Binary_Search/`](06_Binary_Search/)) — 36 problems
6. **Linked List** ([`07_Linked_List/`](07_Linked_List/)) — 24 problems

---

## Solutions

Every solution uses the official LeetCode `class Solution` format with documented pattern, time complexity, and space complexity. Duplicate files are avoided when a problem spans multiple patterns.

### Arrays & Matrix (55)

| # | Problem | Difficulty | Pattern | Time | Space | Solution |
| :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| 1 | Two Sum | Easy | Hashing (Hash Map) | `O(n)` | `O(n)` | [0001_Two_Sum.py](01_Arrays/0001_Two_Sum.py) |
| 26 | Remove Duplicates from Sorted Array | Easy | Two Pointers (In-Place) | `O(n)` | `O(1)` | [0026_Remove_Duplicates_From_Sorted_Array.py](01_Arrays/0026_Remove_Duplicates_From_Sorted_Array.py) |
| 27 | Remove Element | Easy | Two Pointers (In-Place) | `O(n)` | `O(1)` | [0027_Remove_Element.py](01_Arrays/0027_Remove_Element.py) |
| 31 | Next Permutation | Medium | Array Permutation / Two Pointers | `O(n)` | `O(1)` | [0031_Next_Permutation.py](01_Arrays/0031_Next_Permutation.py) |
| 41 | First Missing Positive | Hard | Cyclic Sort / In-Place Index Placement | `O(n)` | `O(1)` | [0041_First_Missing_Positive.py](01_Arrays/0041_First_Missing_Positive.py) |
| 48 | Rotate Image | Medium | Matrix Manipulation (Transpose + Reverse) | `O(n^2)` | `O(1)` | [0048_Rotate_Image.py](01_Arrays/0048_Rotate_Image.py) |
| 53 | Maximum Subarray | Medium | Kadane's Algorithm / Greedy | `O(n)` | `O(1)` | [0053_Maximum_Subarray.py](01_Arrays/0053_Maximum_Subarray.py) |
| 54 | Spiral Matrix | Medium | Matrix Boundary Traversal | `O(m * n)` | `O(1) auxiliary` | [0054_Spiral_Matrix.py](01_Arrays/0054_Spiral_Matrix.py) |
| 55 | Jump Game | Medium | Greedy Reachability | `O(n)` | `O(1)` | [0055_Jump_Game.py](01_Arrays/0055_Jump_Game.py) |
| 56 | Merge Intervals | Medium | Sorting + Interval Merging | `O(n log n)` | `O(n)` | [0056_Merge_Intervals.py](01_Arrays/0056_Merge_Intervals.py) |
| 57 | Insert Interval | Medium | Interval Merging | `O(n)` | `O(n)` | [0057_Insert_Interval.py](01_Arrays/0057_Insert_Interval.py) |
| 59 | Spiral Matrix II | Medium | Matrix Boundary Traversal | `O(n^2)` | `O(1) auxiliary` | [0059_Spiral_Matrix_II.py](01_Arrays/0059_Spiral_Matrix_II.py) |
| 66 | Plus One | Easy | Array Math / Carry Propagation | `O(n)` | `O(1) auxiliary` | [0066_Plus_One.py](01_Arrays/0066_Plus_One.py) |
| 73 | Set Matrix Zeroes | Medium | Matrix In-Place Markers | `O(m * n)` | `O(1)` | [0073_Set_Matrix_Zeroes.py](01_Arrays/0073_Set_Matrix_Zeroes.py) |
