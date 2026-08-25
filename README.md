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
| 75 | Sort Colors | Medium | Three Pointers (Dutch National Flag) | `O(n)` | `O(1)` | [0075_Sort_Colors.py](01_Arrays/0075_Sort_Colors.py) |
| 88 | Merge Sorted Array | Easy | Two Pointers (Reverse Merge) | `O(m + n)` | `O(1)` | [0088_Merge_Sorted_Array.py](01_Arrays/0088_Merge_Sorted_Array.py) |
| 118 | Pascal's Triangle | Easy | Dynamic Programming / Array Construction | `O(numRows^2)` | `O(1) auxiliary` | [0118_Pascals_Triangle.py](01_Arrays/0118_Pascals_Triangle.py) |
| 119 | Pascal's Triangle II | Easy | 1D Rolling Dynamic Programming | `O(rowIndex^2)` | `O(rowIndex)` | [0119_Pascals_Triangle_II.py](01_Arrays/0119_Pascals_Triangle_II.py) |
| 121 | Best Time to Buy and Sell Stock | Easy | Greedy / Running Minimum | `O(n)` | `O(1)` | [0121_Best_Time_To_Buy_And_Sell_Stock.py](01_Arrays/0121_Best_Time_To_Buy_And_Sell_Stock.py) |
| 122 | Best Time to Buy and Sell Stock II | Medium | Greedy | `O(n)` | `O(1)` | [0122_Best_Time_To_Buy_And_Sell_Stock_II.py](01_Arrays/0122_Best_Time_To_Buy_And_Sell_Stock_II.py) |
| 134 | Gas Station | Medium | Greedy | `O(n)` | `O(1)` | [0134_Gas_Station.py](01_Arrays/0134_Gas_Station.py) |
| 135 | Candy | Hard | Greedy (Two-Pass Left/Right Scan) | `O(n)` | `O(n)` | [0135_Candy.py](01_Arrays/0135_Candy.py) |
| 152 | Maximum Product Subarray | Medium | Dynamic Programming / Running Min-Max | `O(n)` | `O(1)` | [0152_Maximum_Product_Subarray.py](01_Arrays/0152_Maximum_Product_Subarray.py) |
| 169 | Majority Element | Easy | Boyer-Moore Voting Algorithm | `O(n)` | `O(1)` | [0169_Majority_Element.py](01_Arrays/0169_Majority_Element.py) |
| 189 | Rotate Array | Medium | Array Reversal | `O(n)` | `O(1)` | [0189_Rotate_Array.py](01_Arrays/0189_Rotate_Array.py) |
| 217 | Contains Duplicate | Easy | Hashing (Hash Set) | `O(n)` | `O(n)` | [0217_Contains_Duplicate.py](01_Arrays/0217_Contains_Duplicate.py) |
| 228 | Summary Ranges | Easy | Array Linear Scan | `O(n)` | `O(1) auxiliary` | [0228_Summary_Ranges.py](01_Arrays/0228_Summary_Ranges.py) |
| 229 | Majority Element II | Medium | Boyer-Moore Voting Algorithm | `O(n)` | `O(1)` | [0229_Majority_Element_II.py](01_Arrays/0229_Majority_Element_II.py) |
| 238 | Product of Array Except Self | Medium | Prefix and Suffix Products | `O(n)` | `O(1) auxiliary` | [0238_Product_Of_Array_Except_Self.py](01_Arrays/0238_Product_Of_Array_Except_Self.py) |
| 240 | Search a 2D Matrix II | Medium | Matrix Staircase Search | `O(m + n)` | `O(1)` | [0240_Search_A_2D_Matrix_II.py](01_Arrays/0240_Search_A_2D_Matrix_II.py) |
| 268 | Missing Number | Easy | Bit Manipulation (XOR) | `O(n)` | `O(1)` | [0268_Missing_Number.py](01_Arrays/0268_Missing_Number.py) |
| 274 | H-Index | Medium | Counting / Bucket Sort | `O(n)` | `O(n)` | [0274_H_Index.py](01_Arrays/0274_H_Index.py) |
| 283 | Move Zeroes | Easy | Two Pointers (In-Place) | `O(n)` | `O(1)` | [0283_Move_Zeroes.py](01_Arrays/0283_Move_Zeroes.py) |
| 289 | Game of Life | Medium | Matrix In-Place State Encoding | `O(m * n)` | `O(1)` | [0289_Game_Of_Life.py](01_Arrays/0289_Game_Of_Life.py) |
| 315 | Count of Smaller Numbers After Self | Hard | Merge Sort / Divide and Conquer | `O(n log n)` | `O(n)` | [0315_Count_Of_Smaller_Numbers_After_Self.py](01_Arrays/0315_Count_Of_Smaller_Numbers_After_Self.py) |
| 330 | Patching Array | Hard | Greedy (Reachable Range) | `O(m + log n)` | `O(1)` | [0330_Patching_Array.py](01_Arrays/0330_Patching_Array.py) |
| 414 | Third Maximum Number | Easy | Array Linear Scan | `O(n)` | `O(1)` | [0414_Third_Maximum_Number.py](01_Arrays/0414_Third_Maximum_Number.py) |
| 442 | Find All Duplicates in an Array | Medium | In-Place Cyclic Marking | `O(n)` | `O(1) auxiliary` | [0442_Find_All_Duplicates_In_An_Array.py](01_Arrays/0442_Find_All_Duplicates_In_An_Array.py) |
| 448 | Find All Numbers Disappeared in an Array | Easy | In-Place Cyclic Marking | `O(n)` | `O(1) auxiliary` | [0448_Find_All_Numbers_Disappeared_In_An_Array.py](01_Arrays/0448_Find_All_Numbers_Disappeared_In_An_Array.py) |
| 485 | Max Consecutive Ones | Easy | Array Linear Scan | `O(n)` | `O(1)` | [0485_Max_Consecutive_Ones.py](01_Arrays/0485_Max_Consecutive_Ones.py) |
| 493 | Reverse Pairs | Hard | Merge Sort / Divide and Conquer | `O(n log n)` | `O(n)` | [0493_Reverse_Pairs.py](01_Arrays/0493_Reverse_Pairs.py) |
| 498 | Diagonal Traverse | Medium | Matrix Diagonal Simulation | `O(m * n)` | `O(1) auxiliary` | [0498_Diagonal_Traverse.py](01_Arrays/0498_Diagonal_Traverse.py) |
| 561 | Array Partition | Easy | Greedy + Sorting | `O(n log n)` | `O(1) auxiliary` | [0561_Array_Partition.py](01_Arrays/0561_Array_Partition.py) |
| 566 | Reshape the Matrix | Easy | Matrix Index Mapping | `O(m * n)` | `O(r * c)` | [0566_Reshape_The_Matrix.py](01_Arrays/0566_Reshape_The_Matrix.py) |
| 605 | Can Place Flowers | Easy | Greedy Array Scan | `O(m)` | `O(1)` | [0605_Can_Place_Flowers.py](01_Arrays/0605_Can_Place_Flowers.py) |
| 628 | Maximum Product of Three Numbers | Easy | Array Linear Scan (Top/Bottom Tracking) | `O(n)` | `O(1)` | [0628_Maximum_Product_Of_Three_Numbers.py](01_Arrays/0628_Maximum_Product_Of_Three_Numbers.py) |
| 645 | Set Mismatch | Easy | In-Place Cyclic Marking | `O(n)` | `O(1) auxiliary` | [0645_Set_Mismatch.py](01_Arrays/0645_Set_Mismatch.py) |
| 724 | Find Pivot Index | Easy | Prefix Sum | `O(n)` | `O(1)` | [0724_Find_Pivot_Index.py](01_Arrays/0724_Find_Pivot_Index.py) |
| 867 | Transpose Matrix | Easy | Matrix Manipulation | `O(m * n)` | `O(m * n)` | [0867_Transpose_Matrix.py](01_Arrays/0867_Transpose_Matrix.py) |
| 918 | Maximum Sum Circular Subarray | Medium | Kadane's Algorithm (Circular Variant) | `O(n)` | `O(1)` | [0918_Maximum_Sum_Circular_Subarray.py](01_Arrays/0918_Maximum_Sum_Circular_Subarray.py) |
| 977 | Squares of a Sorted Array | Easy | Two Pointers | `O(n)` | `O(n)` | [0977_Squares_Of_A_Sorted_Array.py](01_Arrays/0977_Squares_Of_A_Sorted_Array.py) |
| 1013 | Partition Array Into Three Parts With Equal Sum | Easy | Prefix Sum / Greedy | `O(n)` | `O(1)` | [1013_Partition_Array_Into_Three_Parts_With_Equal_Sum.py](01_Arrays/1013_Partition_Array_Into_Three_Parts_With_Equal_Sum.py) |
| 1299 | Replace Elements with Greatest Element on Right Side | Easy | Array Reverse Scan | `O(n)` | `O(1) auxiliary` | [1299_Replace_Elements_With_Greatest_Element_On_Right_Side.py](01_Arrays/1299_Replace_Elements_With_Greatest_Element_On_Right_Side.py) |
| 1480 | Running Sum of 1d Array | Easy | Prefix Sum | `O(n)` | `O(1) auxiliary` | [1480_Running_Sum_Of_1d_Array.py](01_Arrays/1480_Running_Sum_Of_1d_Array.py) |
| 1672 | Richest Customer Wealth | Easy | Matrix Row Sum | `O(m * n)` | `O(1)` | [1672_Richest_Customer_Wealth.py](01_Arrays/1672_Richest_Customer_Wealth.py) |

### Hashing (40)

| # | Problem | Difficulty | Pattern | Time | Space | Solution |
| :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| 36 | Valid Sudoku | Medium | Hashing (Hash Set) | `O(1)` | `O(1)` | [0036_Valid_Sudoku.py](03_Hashing/0036_Valid_Sudoku.py) |
| 49 | Group Anagrams | Medium | Hashing (Character Frequency Key) | `O(n * k)` | `O(n * k)` | [0049_Group_Anagrams.py](03_Hashing/0049_Group_Anagrams.py) |
| 128 | Longest Consecutive Sequence | Medium | Hashing (Hash Set) | `O(n)` | `O(n)` | [0128_Longest_Consecutive_Sequence.py](03_Hashing/0128_Longest_Consecutive_Sequence.py) |
| 136 | Single Number | Easy | Bit Manipulation (XOR) | `O(n)` | `O(1)` | [0136_Single_Number.py](03_Hashing/0136_Single_Number.py) |
| 149 | Max Points on a Line | Hard | Hashing (Slope Frequency Map) | `O(n^2)` | `O(n)` | [0149_Max_Points_On_A_Line.py](03_Hashing/0149_Max_Points_On_A_Line.py) |
| 187 | Repeated DNA Sequences | Medium | Hashing (Hash Set) | `O(n)` | `O(n)` | [0187_Repeated_DNA_Sequences.py](03_Hashing/0187_Repeated_DNA_Sequences.py) |
| 202 | Happy Number | Easy | Hashing (Cycle Detection with Hash Set) | `O(log n)` | `O(log n)` | [0202_Happy_Number.py](03_Hashing/0202_Happy_Number.py) |
| 205 | Isomorphic Strings | Easy | Hashing (Bijective Mapping) | `O(n)` | `O(1)` | [0205_Isomorphic_Strings.py](03_Hashing/0205_Isomorphic_Strings.py) |
| 219 | Contains Duplicate II | Easy | Hashing (Last Seen Index) | `O(n)` | `O(n)` | [0219_Contains_Duplicate_II.py](03_Hashing/0219_Contains_Duplicate_II.py) |
| 242 | Valid Anagram | Easy | Hashing (Frequency Counting) | `O(n)` | `O(1)` | [0242_Valid_Anagram.py](03_Hashing/0242_Valid_Anagram.py) |
| 290 | Word Pattern | Easy | Hashing (Bijective Mapping) | `O(n + m)` | `O(n + m)` | [0290_Word_Pattern.py](03_Hashing/0290_Word_Pattern.py) |
| 299 | Bulls and Cows | Medium | Hashing (Frequency Counting) | `O(n)` | `O(1)` | [0299_Bulls_And_Cows.py](03_Hashing/0299_Bulls_And_Cows.py) |
| 349 | Intersection of Two Arrays | Easy | Hashing (Hash Set) | `O(n + m)` | `O(min(n, m))` | [0349_Intersection_Of_Two_Arrays.py](03_Hashing/0349_Intersection_Of_Two_Arrays.py) |
| 350 | Intersection of Two Arrays II | Easy | Hashing (Frequency Counter) | `O(n + m)` | `O(min(n, m))` | [0350_Intersection_Of_Two_Arrays_II.py](03_Hashing/0350_Intersection_Of_Two_Arrays_II.py) |
| 383 | Ransom Note | Easy | Hashing (Frequency Counting) | `O(n + m)` | `O(1)` | [0383_Ransom_Note.py](03_Hashing/0383_Ransom_Note.py) |
| 387 | First Unique Character in a String | Easy | Hashing (Frequency Counting) | `O(n)` | `O(1)` | [0387_First_Unique_Character_In_A_String.py](03_Hashing/0387_First_Unique_Character_In_A_String.py) |
| 389 | Find the Difference | Easy | Bit Manipulation (XOR) / Hashing | `O(n)` | `O(1)` | [0389_Find_The_Difference.py](03_Hashing/0389_Find_The_Difference.py) |
| 409 | Longest Palindrome | Easy | Hashing (Frequency Counting) | `O(n)` | `O(1)` | [0409_Longest_Palindrome.py](03_Hashing/0409_Longest_Palindrome.py) |
| 447 | Number of Boomerangs | Medium | Hashing (Distance Frequency Map) | `O(n^2)` | `O(n)` | [0447_Number_Of_Boomerangs.py](03_Hashing/0447_Number_Of_Boomerangs.py) |
| 451 | Sort Characters By Frequency | Medium | Hashing + Bucket Sort | `O(n)` | `O(n)` | [0451_Sort_Characters_By_Frequency.py](03_Hashing/0451_Sort_Characters_By_Frequency.py) |
| 454 | 4Sum II | Medium | Hashing (Hash Map Pair Sums) | `O(n^2)` | `O(n^2)` | [0454_4Sum_II.py](03_Hashing/0454_4Sum_II.py) |
| 500 | Keyboard Row | Easy | Hashing (Hash Set) | `O(total chars)` | `O(1)` | [0500_Keyboard_Row.py](03_Hashing/0500_Keyboard_Row.py) |
| 523 | Continuous Subarray Sum | Medium | Prefix Sum + Hash Map | `O(n)` | `O(min(n, k))` | [0523_Continuous_Subarray_Sum.py](03_Hashing/0523_Continuous_Subarray_Sum.py) |
| 525 | Contiguous Array | Medium | Prefix Sum + Hash Map | `O(n)` | `O(n)` | [0525_Contiguous_Array.py](03_Hashing/0525_Contiguous_Array.py) |
| 532 | K-diff Pairs in an Array | Medium | Hashing (Frequency Counter) | `O(n)` | `O(n)` | [0532_K_Diff_Pairs_In_An_Array.py](03_Hashing/0532_K_Diff_Pairs_In_An_Array.py) |
| 554 | Brick Wall | Medium | Hashing (Edge Frequency Map) | `O(total bricks)` | `O(width)` | [0554_Brick_Wall.py](03_Hashing/0554_Brick_Wall.py) |
| 560 | Subarray Sum Equals K | Medium | Prefix Sum + Hash Map | `O(n)` | `O(n)` | [0560_Subarray_Sum_Equals_K.py](03_Hashing/0560_Subarray_Sum_Equals_K.py) |
| 594 | Longest Harmonious Subsequence | Easy | Hashing (Frequency Counter) | `O(n)` | `O(n)` | [0594_Longest_Harmonious_Subsequence.py](03_Hashing/0594_Longest_Harmonious_Subsequence.py) |
| 599 | Minimum Index Sum of Two Lists | Easy | Hashing (Index Map) | `O(n + m)` | `O(n)` | [0599_Minimum_Index_Sum_Of_Two_Lists.py](03_Hashing/0599_Minimum_Index_Sum_Of_Two_Lists.py) |
| 692 | Top K Frequent Words | Medium | Hashing + Sorting | `O(n log n)` | `O(n)` | [0692_Top_K_Frequent_Words.py](03_Hashing/0692_Top_K_Frequent_Words.py) |
| 771 | Jewels and Stones | Easy | Hashing (Hash Set) | `O(J + S)` | `O(J)` | [0771_Jewels_And_Stones.py](03_Hashing/0771_Jewels_And_Stones.py) |
| 791 | Custom Sort String | Medium | Hashing (Frequency Counting) | `O(n + m)` | `O(n)` | [0791_Custom_Sort_String.py](03_Hashing/0791_Custom_Sort_String.py) |
| 819 | Most Common Word | Easy | Hashing (Frequency Counter + Hash Set) | `O(n + m)` | `O(n + m)` | [0819_Most_Common_Word.py](03_Hashing/0819_Most_Common_Word.py) |
| 884 | Uncommon Words from Two Sentences | Easy | Hashing (Frequency Counting) | `O(n + m)` | `O(n + m)` | [0884_Uncommon_Words_From_Two_Sentences.py](03_Hashing/0884_Uncommon_Words_From_Two_Sentences.py) |
| 974 | Subarray Sums Divisible by K | Medium | Prefix Sum + Hash Map | `O(n)` | `O(k)` | [0974_Subarray_Sums_Divisible_By_K.py](03_Hashing/0974_Subarray_Sums_Divisible_By_K.py) |
| 1002 | Find Common Characters | Easy | Hashing (Frequency Intersection) | `O(n * k)` | `O(1)` | [1002_Find_Common_Characters.py](03_Hashing/1002_Find_Common_Characters.py) |
| 1074 | Number of Submatrices That Sum to Target | Hard | Prefix Sum + Hash Map (2D Reduction) | `O(rows^2 * cols)` | `O(cols)` | [1074_Number_Of_Submatrices_That_Sum_To_Target.py](03_Hashing/1074_Number_Of_Submatrices_That_Sum_To_Target.py) |
| 1160 | Find Words That Can Be Formed by Characters | Easy | Hashing (Frequency Counting) | `O(total chars)` | `O(1)` | [1160_Find_Words_That_Can_Be_Formed_By_Characters.py](03_Hashing/1160_Find_Words_That_Can_Be_Formed_By_Characters.py) |
| 1207 | Unique Number of Occurrences | Easy | Hashing (Hash Map + Hash Set) | `O(n)` | `O(n)` | [1207_Unique_Number_Of_Occurrences.py](03_Hashing/1207_Unique_Number_Of_Occurrences.py) |
| 1394 | Find Lucky Integer in an Array | Easy | Hashing (Frequency Counter) | `O(n)` | `O(n)` | [1394_Find_Lucky_Integer_In_An_Array.py](03_Hashing/1394_Find_Lucky_Integer_In_An_Array.py) |

### Two Pointers (30)

| # | Problem | Difficulty | Pattern | Time | Space | Solution |
| :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| 5 | Longest Palindromic Substring | Medium | Two Pointers (Expand Around Center) | `O(n^2)` | `O(1)` | [0005_Longest_Palindromic_Substring.py](04_Two_Pointers/0005_Longest_Palindromic_Substring.py) |
| 11 | Container With Most Water | Medium | Two Pointers (Opposite Ends) | `O(n)` | `O(1)` | [0011_Container_With_Most_Water.py](04_Two_Pointers/0011_Container_With_Most_Water.py) |
| 15 | 3Sum | Medium | Two Pointers + Sorting | `O(n^2)` | `O(1) auxiliary` | [0015_3Sum.py](04_Two_Pointers/0015_3Sum.py) |
| 16 | 3Sum Closest | Medium | Two Pointers + Sorting | `O(n^2)` | `O(1) auxiliary` | [0016_3Sum_Closest.py](04_Two_Pointers/0016_3Sum_Closest.py) |
| 18 | 4Sum | Medium | Two Pointers + Sorting | `O(n^3)` | `O(1) auxiliary` | [0018_4Sum.py](04_Two_Pointers/0018_4Sum.py) |
| 28 | Find the Index of the First Occurrence in a String | Easy | Two Pointers / String Matching | `O(n * m)` | `O(1)` | [0028_Find_The_Index_Of_The_First_Occurrence_In_A_String.py](04_Two_Pointers/0028_Find_The_Index_Of_The_First_Occurrence_In_A_String.py) |
| 42 | Trapping Rain Water | Hard | Two Pointers (Opposite Ends) | `O(n)` | `O(1)` | [0042_Trapping_Rain_Water.py](04_Two_Pointers/0042_Trapping_Rain_Water.py) |
| 80 | Remove Duplicates from Sorted Array II | Medium | Two Pointers (In-Place) | `O(n)` | `O(1)` | [0080_Remove_Duplicates_From_Sorted_Array_II.py](04_Two_Pointers/0080_Remove_Duplicates_From_Sorted_Array_II.py) |
| 125 | Valid Palindrome | Easy | Two Pointers (Opposite Ends) | `O(n)` | `O(1)` | [0125_Valid_Palindrome.py](04_Two_Pointers/0125_Valid_Palindrome.py) |
| 151 | Reverse Words in a String | Medium | Two Pointers | `O(n)` | `O(n)` | [0151_Reverse_Words_In_A_String.py](04_Two_Pointers/0151_Reverse_Words_In_A_String.py) |
| 167 | Two Sum II - Input Array Is Sorted | Medium | Two Pointers (Opposite Ends) | `O(n)` | `O(1)` | [0167_Two_Sum_II_Input_Array_Is_Sorted.py](04_Two_Pointers/0167_Two_Sum_II_Input_Array_Is_Sorted.py) |
