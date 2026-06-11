# Problem Tracker

Complete tracker of all **218 unique problems** implemented and tested in Python across 6 core DSA topics.

## Summary

- **Total Implemented & Tested:** 218
- **Difficulty Breakdown:** 84 Easy | 112 Medium | 22 Hard

## Arrays & Matrix (`01_Arrays/`) — 55 Problems
*Easy: 28 | Medium: 22 | Hard: 5*

| # | Title | Difficulty | Pattern | Time | Space | Status | Solution |
| :---: | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
| 1 | Two Sum | Easy | Hashing (Hash Map) | `O(n)` | `O(n)` | Implemented & Tested | [0001_Two_Sum.py](../01_Arrays/0001_Two_Sum.py) |
| 26 | Remove Duplicates from Sorted Array | Easy | Two Pointers (In-Place) | `O(n)` | `O(1)` | Implemented & Tested | [0026_Remove_Duplicates_From_Sorted_Array.py](../01_Arrays/0026_Remove_Duplicates_From_Sorted_Array.py) |
| 27 | Remove Element | Easy | Two Pointers (In-Place) | `O(n)` | `O(1)` | Implemented & Tested | [0027_Remove_Element.py](../01_Arrays/0027_Remove_Element.py) |
| 31 | Next Permutation | Medium | Array Permutation / Two Pointers | `O(n)` | `O(1)` | Implemented & Tested | [0031_Next_Permutation.py](../01_Arrays/0031_Next_Permutation.py) |
| 41 | First Missing Positive | Hard | Cyclic Sort / In-Place Index Placement | `O(n)` | `O(1)` | Implemented & Tested | [0041_First_Missing_Positive.py](../01_Arrays/0041_First_Missing_Positive.py) |
| 48 | Rotate Image | Medium | Matrix Manipulation (Transpose + Reverse) | `O(n^2)` | `O(1)` | Implemented & Tested | [0048_Rotate_Image.py](../01_Arrays/0048_Rotate_Image.py) |
| 53 | Maximum Subarray | Medium | Kadane's Algorithm / Greedy | `O(n)` | `O(1)` | Implemented & Tested | [0053_Maximum_Subarray.py](../01_Arrays/0053_Maximum_Subarray.py) |
| 54 | Spiral Matrix | Medium | Matrix Boundary Traversal | `O(m * n)` | `O(1) auxiliary` | Implemented & Tested | [0054_Spiral_Matrix.py](../01_Arrays/0054_Spiral_Matrix.py) |
| 55 | Jump Game | Medium | Greedy Reachability | `O(n)` | `O(1)` | Implemented & Tested | [0055_Jump_Game.py](../01_Arrays/0055_Jump_Game.py) |
| 56 | Merge Intervals | Medium | Sorting + Interval Merging | `O(n log n)` | `O(n)` | Implemented & Tested | [0056_Merge_Intervals.py](../01_Arrays/0056_Merge_Intervals.py) |
| 57 | Insert Interval | Medium | Interval Merging | `O(n)` | `O(n)` | Implemented & Tested | [0057_Insert_Interval.py](../01_Arrays/0057_Insert_Interval.py) |
| 59 | Spiral Matrix II | Medium | Matrix Boundary Traversal | `O(n^2)` | `O(1) auxiliary` | Implemented & Tested | [0059_Spiral_Matrix_II.py](../01_Arrays/0059_Spiral_Matrix_II.py) |
| 66 | Plus One | Easy | Array Math / Carry Propagation | `O(n)` | `O(1) auxiliary` | Implemented & Tested | [0066_Plus_One.py](../01_Arrays/0066_Plus_One.py) |
| 73 | Set Matrix Zeroes | Medium | Matrix In-Place Markers | `O(m * n)` | `O(1)` | Implemented & Tested | [0073_Set_Matrix_Zeroes.py](../01_Arrays/0073_Set_Matrix_Zeroes.py) |
| 75 | Sort Colors | Medium | Three Pointers (Dutch National Flag) | `O(n)` | `O(1)` | Implemented & Tested | [0075_Sort_Colors.py](../01_Arrays/0075_Sort_Colors.py) |
| 88 | Merge Sorted Array | Easy | Two Pointers (Reverse Merge) | `O(m + n)` | `O(1)` | Implemented & Tested | [0088_Merge_Sorted_Array.py](../01_Arrays/0088_Merge_Sorted_Array.py) |
| 118 | Pascal's Triangle | Easy | Dynamic Programming / Array Construction | `O(numRows^2)` | `O(1) auxiliary` | Implemented & Tested | [0118_Pascals_Triangle.py](../01_Arrays/0118_Pascals_Triangle.py) |
| 119 | Pascal's Triangle II | Easy | 1D Rolling Dynamic Programming | `O(rowIndex^2)` | `O(rowIndex)` | Implemented & Tested | [0119_Pascals_Triangle_II.py](../01_Arrays/0119_Pascals_Triangle_II.py) |
| 121 | Best Time to Buy and Sell Stock | Easy | Greedy / Running Minimum | `O(n)` | `O(1)` | Implemented & Tested | [0121_Best_Time_To_Buy_And_Sell_Stock.py](../01_Arrays/0121_Best_Time_To_Buy_And_Sell_Stock.py) |
| 122 | Best Time to Buy and Sell Stock II | Medium | Greedy | `O(n)` | `O(1)` | Implemented & Tested | [0122_Best_Time_To_Buy_And_Sell_Stock_II.py](../01_Arrays/0122_Best_Time_To_Buy_And_Sell_Stock_II.py) |
| 134 | Gas Station | Medium | Greedy | `O(n)` | `O(1)` | Implemented & Tested | [0134_Gas_Station.py](../01_Arrays/0134_Gas_Station.py) |
| 135 | Candy | Hard | Greedy (Two-Pass Left/Right Scan) | `O(n)` | `O(n)` | Implemented & Tested | [0135_Candy.py](../01_Arrays/0135_Candy.py) |
| 152 | Maximum Product Subarray | Medium | Dynamic Programming / Running Min-Max | `O(n)` | `O(1)` | Implemented & Tested | [0152_Maximum_Product_Subarray.py](../01_Arrays/0152_Maximum_Product_Subarray.py) |
| 169 | Majority Element | Easy | Boyer-Moore Voting Algorithm | `O(n)` | `O(1)` | Implemented & Tested | [0169_Majority_Element.py](../01_Arrays/0169_Majority_Element.py) |
| 189 | Rotate Array | Medium | Array Reversal | `O(n)` | `O(1)` | Implemented & Tested | [0189_Rotate_Array.py](../01_Arrays/0189_Rotate_Array.py) |
| 217 | Contains Duplicate | Easy | Hashing (Hash Set) | `O(n)` | `O(n)` | Implemented & Tested | [0217_Contains_Duplicate.py](../01_Arrays/0217_Contains_Duplicate.py) |
| 228 | Summary Ranges | Easy | Array Linear Scan | `O(n)` | `O(1) auxiliary` | Implemented & Tested | [0228_Summary_Ranges.py](../01_Arrays/0228_Summary_Ranges.py) |
| 229 | Majority Element II | Medium | Boyer-Moore Voting Algorithm | `O(n)` | `O(1)` | Implemented & Tested | [0229_Majority_Element_II.py](../01_Arrays/0229_Majority_Element_II.py) |
| 238 | Product of Array Except Self | Medium | Prefix and Suffix Products | `O(n)` | `O(1) auxiliary` | Implemented & Tested | [0238_Product_Of_Array_Except_Self.py](../01_Arrays/0238_Product_Of_Array_Except_Self.py) |
| 240 | Search a 2D Matrix II | Medium | Matrix Staircase Search | `O(m + n)` | `O(1)` | Implemented & Tested | [0240_Search_A_2D_Matrix_II.py](../01_Arrays/0240_Search_A_2D_Matrix_II.py) |
| 268 | Missing Number | Easy | Bit Manipulation (XOR) | `O(n)` | `O(1)` | Implemented & Tested | [0268_Missing_Number.py](../01_Arrays/0268_Missing_Number.py) |
| 274 | H-Index | Medium | Counting / Bucket Sort | `O(n)` | `O(n)` | Implemented & Tested | [0274_H_Index.py](../01_Arrays/0274_H_Index.py) |
| 283 | Move Zeroes | Easy | Two Pointers (In-Place) | `O(n)` | `O(1)` | Implemented & Tested | [0283_Move_Zeroes.py](../01_Arrays/0283_Move_Zeroes.py) |
| 289 | Game of Life | Medium | Matrix In-Place State Encoding | `O(m * n)` | `O(1)` | Implemented & Tested | [0289_Game_Of_Life.py](../01_Arrays/0289_Game_Of_Life.py) |
| 315 | Count of Smaller Numbers After Self | Hard | Merge Sort / Divide and Conquer | `O(n log n)` | `O(n)` | Implemented & Tested | [0315_Count_Of_Smaller_Numbers_After_Self.py](../01_Arrays/0315_Count_Of_Smaller_Numbers_After_Self.py) |
| 330 | Patching Array | Hard | Greedy (Reachable Range) | `O(m + log n)` | `O(1)` | Implemented & Tested | [0330_Patching_Array.py](../01_Arrays/0330_Patching_Array.py) |
