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
| 414 | Third Maximum Number | Easy | Array Linear Scan | `O(n)` | `O(1)` | Implemented & Tested | [0414_Third_Maximum_Number.py](../01_Arrays/0414_Third_Maximum_Number.py) |
| 442 | Find All Duplicates in an Array | Medium | In-Place Cyclic Marking | `O(n)` | `O(1) auxiliary` | Implemented & Tested | [0442_Find_All_Duplicates_In_An_Array.py](../01_Arrays/0442_Find_All_Duplicates_In_An_Array.py) |
| 448 | Find All Numbers Disappeared in an Array | Easy | In-Place Cyclic Marking | `O(n)` | `O(1) auxiliary` | Implemented & Tested | [0448_Find_All_Numbers_Disappeared_In_An_Array.py](../01_Arrays/0448_Find_All_Numbers_Disappeared_In_An_Array.py) |
| 485 | Max Consecutive Ones | Easy | Array Linear Scan | `O(n)` | `O(1)` | Implemented & Tested | [0485_Max_Consecutive_Ones.py](../01_Arrays/0485_Max_Consecutive_Ones.py) |
| 493 | Reverse Pairs | Hard | Merge Sort / Divide and Conquer | `O(n log n)` | `O(n)` | Implemented & Tested | [0493_Reverse_Pairs.py](../01_Arrays/0493_Reverse_Pairs.py) |
| 498 | Diagonal Traverse | Medium | Matrix Diagonal Simulation | `O(m * n)` | `O(1) auxiliary` | Implemented & Tested | [0498_Diagonal_Traverse.py](../01_Arrays/0498_Diagonal_Traverse.py) |
| 561 | Array Partition | Easy | Greedy + Sorting | `O(n log n)` | `O(1) auxiliary` | Implemented & Tested | [0561_Array_Partition.py](../01_Arrays/0561_Array_Partition.py) |
| 566 | Reshape the Matrix | Easy | Matrix Index Mapping | `O(m * n)` | `O(r * c)` | Implemented & Tested | [0566_Reshape_The_Matrix.py](../01_Arrays/0566_Reshape_The_Matrix.py) |
| 605 | Can Place Flowers | Easy | Greedy Array Scan | `O(m)` | `O(1)` | Implemented & Tested | [0605_Can_Place_Flowers.py](../01_Arrays/0605_Can_Place_Flowers.py) |
| 628 | Maximum Product of Three Numbers | Easy | Array Linear Scan (Top/Bottom Tracking) | `O(n)` | `O(1)` | Implemented & Tested | [0628_Maximum_Product_Of_Three_Numbers.py](../01_Arrays/0628_Maximum_Product_Of_Three_Numbers.py) |
| 645 | Set Mismatch | Easy | In-Place Cyclic Marking | `O(n)` | `O(1) auxiliary` | Implemented & Tested | [0645_Set_Mismatch.py](../01_Arrays/0645_Set_Mismatch.py) |
| 724 | Find Pivot Index | Easy | Prefix Sum | `O(n)` | `O(1)` | Implemented & Tested | [0724_Find_Pivot_Index.py](../01_Arrays/0724_Find_Pivot_Index.py) |
| 867 | Transpose Matrix | Easy | Matrix Manipulation | `O(m * n)` | `O(m * n)` | Implemented & Tested | [0867_Transpose_Matrix.py](../01_Arrays/0867_Transpose_Matrix.py) |
| 918 | Maximum Sum Circular Subarray | Medium | Kadane's Algorithm (Circular Variant) | `O(n)` | `O(1)` | Implemented & Tested | [0918_Maximum_Sum_Circular_Subarray.py](../01_Arrays/0918_Maximum_Sum_Circular_Subarray.py) |
| 977 | Squares of a Sorted Array | Easy | Two Pointers | `O(n)` | `O(n)` | Implemented & Tested | [0977_Squares_Of_A_Sorted_Array.py](../01_Arrays/0977_Squares_Of_A_Sorted_Array.py) |
| 1013 | Partition Array Into Three Parts With Equal Sum | Easy | Prefix Sum / Greedy | `O(n)` | `O(1)` | Implemented & Tested | [1013_Partition_Array_Into_Three_Parts_With_Equal_Sum.py](../01_Arrays/1013_Partition_Array_Into_Three_Parts_With_Equal_Sum.py) |
| 1299 | Replace Elements with Greatest Element on Right Side | Easy | Array Reverse Scan | `O(n)` | `O(1) auxiliary` | Implemented & Tested | [1299_Replace_Elements_With_Greatest_Element_On_Right_Side.py](../01_Arrays/1299_Replace_Elements_With_Greatest_Element_On_Right_Side.py) |
| 1480 | Running Sum of 1d Array | Easy | Prefix Sum | `O(n)` | `O(1) auxiliary` | Implemented & Tested | [1480_Running_Sum_Of_1d_Array.py](../01_Arrays/1480_Running_Sum_Of_1d_Array.py) |
| 1672 | Richest Customer Wealth | Easy | Matrix Row Sum | `O(m * n)` | `O(1)` | Implemented & Tested | [1672_Richest_Customer_Wealth.py](../01_Arrays/1672_Richest_Customer_Wealth.py) |

## Hashing (`03_Hashing/`) — 40 Problems
*Easy: 22 | Medium: 16 | Hard: 2*

| # | Title | Difficulty | Pattern | Time | Space | Status | Solution |
| :---: | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
| 36 | Valid Sudoku | Medium | Hashing (Hash Set) | `O(1)` | `O(1)` | Implemented & Tested | [0036_Valid_Sudoku.py](../03_Hashing/0036_Valid_Sudoku.py) |
| 49 | Group Anagrams | Medium | Hashing (Character Frequency Key) | `O(n * k)` | `O(n * k)` | Implemented & Tested | [0049_Group_Anagrams.py](../03_Hashing/0049_Group_Anagrams.py) |
| 128 | Longest Consecutive Sequence | Medium | Hashing (Hash Set) | `O(n)` | `O(n)` | Implemented & Tested | [0128_Longest_Consecutive_Sequence.py](../03_Hashing/0128_Longest_Consecutive_Sequence.py) |
| 136 | Single Number | Easy | Bit Manipulation (XOR) | `O(n)` | `O(1)` | Implemented & Tested | [0136_Single_Number.py](../03_Hashing/0136_Single_Number.py) |
| 149 | Max Points on a Line | Hard | Hashing (Slope Frequency Map) | `O(n^2)` | `O(n)` | Implemented & Tested | [0149_Max_Points_On_A_Line.py](../03_Hashing/0149_Max_Points_On_A_Line.py) |
| 187 | Repeated DNA Sequences | Medium | Hashing (Hash Set) | `O(n)` | `O(n)` | Implemented & Tested | [0187_Repeated_DNA_Sequences.py](../03_Hashing/0187_Repeated_DNA_Sequences.py) |
| 202 | Happy Number | Easy | Hashing (Cycle Detection with Hash Set) | `O(log n)` | `O(log n)` | Implemented & Tested | [0202_Happy_Number.py](../03_Hashing/0202_Happy_Number.py) |
| 205 | Isomorphic Strings | Easy | Hashing (Bijective Mapping) | `O(n)` | `O(1)` | Implemented & Tested | [0205_Isomorphic_Strings.py](../03_Hashing/0205_Isomorphic_Strings.py) |
| 219 | Contains Duplicate II | Easy | Hashing (Last Seen Index) | `O(n)` | `O(n)` | Implemented & Tested | [0219_Contains_Duplicate_II.py](../03_Hashing/0219_Contains_Duplicate_II.py) |
| 242 | Valid Anagram | Easy | Hashing (Frequency Counting) | `O(n)` | `O(1)` | Implemented & Tested | [0242_Valid_Anagram.py](../03_Hashing/0242_Valid_Anagram.py) |
| 290 | Word Pattern | Easy | Hashing (Bijective Mapping) | `O(n + m)` | `O(n + m)` | Implemented & Tested | [0290_Word_Pattern.py](../03_Hashing/0290_Word_Pattern.py) |
| 299 | Bulls and Cows | Medium | Hashing (Frequency Counting) | `O(n)` | `O(1)` | Implemented & Tested | [0299_Bulls_And_Cows.py](../03_Hashing/0299_Bulls_And_Cows.py) |
| 349 | Intersection of Two Arrays | Easy | Hashing (Hash Set) | `O(n + m)` | `O(min(n, m))` | Implemented & Tested | [0349_Intersection_Of_Two_Arrays.py](../03_Hashing/0349_Intersection_Of_Two_Arrays.py) |
| 350 | Intersection of Two Arrays II | Easy | Hashing (Frequency Counter) | `O(n + m)` | `O(min(n, m))` | Implemented & Tested | [0350_Intersection_Of_Two_Arrays_II.py](../03_Hashing/0350_Intersection_Of_Two_Arrays_II.py) |
| 383 | Ransom Note | Easy | Hashing (Frequency Counting) | `O(n + m)` | `O(1)` | Implemented & Tested | [0383_Ransom_Note.py](../03_Hashing/0383_Ransom_Note.py) |
| 387 | First Unique Character in a String | Easy | Hashing (Frequency Counting) | `O(n)` | `O(1)` | Implemented & Tested | [0387_First_Unique_Character_In_A_String.py](../03_Hashing/0387_First_Unique_Character_In_A_String.py) |
| 389 | Find the Difference | Easy | Bit Manipulation (XOR) / Hashing | `O(n)` | `O(1)` | Implemented & Tested | [0389_Find_The_Difference.py](../03_Hashing/0389_Find_The_Difference.py) |
| 409 | Longest Palindrome | Easy | Hashing (Frequency Counting) | `O(n)` | `O(1)` | Implemented & Tested | [0409_Longest_Palindrome.py](../03_Hashing/0409_Longest_Palindrome.py) |
| 447 | Number of Boomerangs | Medium | Hashing (Distance Frequency Map) | `O(n^2)` | `O(n)` | Implemented & Tested | [0447_Number_Of_Boomerangs.py](../03_Hashing/0447_Number_Of_Boomerangs.py) |
| 451 | Sort Characters By Frequency | Medium | Hashing + Bucket Sort | `O(n)` | `O(n)` | Implemented & Tested | [0451_Sort_Characters_By_Frequency.py](../03_Hashing/0451_Sort_Characters_By_Frequency.py) |
| 454 | 4Sum II | Medium | Hashing (Hash Map Pair Sums) | `O(n^2)` | `O(n^2)` | Implemented & Tested | [0454_4Sum_II.py](../03_Hashing/0454_4Sum_II.py) |
| 500 | Keyboard Row | Easy | Hashing (Hash Set) | `O(total chars)` | `O(1)` | Implemented & Tested | [0500_Keyboard_Row.py](../03_Hashing/0500_Keyboard_Row.py) |
| 523 | Continuous Subarray Sum | Medium | Prefix Sum + Hash Map | `O(n)` | `O(min(n, k))` | Implemented & Tested | [0523_Continuous_Subarray_Sum.py](../03_Hashing/0523_Continuous_Subarray_Sum.py) |
| 525 | Contiguous Array | Medium | Prefix Sum + Hash Map | `O(n)` | `O(n)` | Implemented & Tested | [0525_Contiguous_Array.py](../03_Hashing/0525_Contiguous_Array.py) |
| 532 | K-diff Pairs in an Array | Medium | Hashing (Frequency Counter) | `O(n)` | `O(n)` | Implemented & Tested | [0532_K_Diff_Pairs_In_An_Array.py](../03_Hashing/0532_K_Diff_Pairs_In_An_Array.py) |
| 554 | Brick Wall | Medium | Hashing (Edge Frequency Map) | `O(total bricks)` | `O(width)` | Implemented & Tested | [0554_Brick_Wall.py](../03_Hashing/0554_Brick_Wall.py) |
| 560 | Subarray Sum Equals K | Medium | Prefix Sum + Hash Map | `O(n)` | `O(n)` | Implemented & Tested | [0560_Subarray_Sum_Equals_K.py](../03_Hashing/0560_Subarray_Sum_Equals_K.py) |
| 594 | Longest Harmonious Subsequence | Easy | Hashing (Frequency Counter) | `O(n)` | `O(n)` | Implemented & Tested | [0594_Longest_Harmonious_Subsequence.py](../03_Hashing/0594_Longest_Harmonious_Subsequence.py) |
| 599 | Minimum Index Sum of Two Lists | Easy | Hashing (Index Map) | `O(n + m)` | `O(n)` | Implemented & Tested | [0599_Minimum_Index_Sum_Of_Two_Lists.py](../03_Hashing/0599_Minimum_Index_Sum_Of_Two_Lists.py) |
| 692 | Top K Frequent Words | Medium | Hashing + Sorting | `O(n log n)` | `O(n)` | Implemented & Tested | [0692_Top_K_Frequent_Words.py](../03_Hashing/0692_Top_K_Frequent_Words.py) |
| 771 | Jewels and Stones | Easy | Hashing (Hash Set) | `O(J + S)` | `O(J)` | Implemented & Tested | [0771_Jewels_And_Stones.py](../03_Hashing/0771_Jewels_And_Stones.py) |
| 791 | Custom Sort String | Medium | Hashing (Frequency Counting) | `O(n + m)` | `O(n)` | Implemented & Tested | [0791_Custom_Sort_String.py](../03_Hashing/0791_Custom_Sort_String.py) |
| 819 | Most Common Word | Easy | Hashing (Frequency Counter + Hash Set) | `O(n + m)` | `O(n + m)` | Implemented & Tested | [0819_Most_Common_Word.py](../03_Hashing/0819_Most_Common_Word.py) |
| 884 | Uncommon Words from Two Sentences | Easy | Hashing (Frequency Counting) | `O(n + m)` | `O(n + m)` | Implemented & Tested | [0884_Uncommon_Words_From_Two_Sentences.py](../03_Hashing/0884_Uncommon_Words_From_Two_Sentences.py) |
| 974 | Subarray Sums Divisible by K | Medium | Prefix Sum + Hash Map | `O(n)` | `O(k)` | Implemented & Tested | [0974_Subarray_Sums_Divisible_By_K.py](../03_Hashing/0974_Subarray_Sums_Divisible_By_K.py) |
| 1002 | Find Common Characters | Easy | Hashing (Frequency Intersection) | `O(n * k)` | `O(1)` | Implemented & Tested | [1002_Find_Common_Characters.py](../03_Hashing/1002_Find_Common_Characters.py) |
| 1074 | Number of Submatrices That Sum to Target | Hard | Prefix Sum + Hash Map (2D Reduction) | `O(rows^2 * cols)` | `O(cols)` | Implemented & Tested | [1074_Number_Of_Submatrices_That_Sum_To_Target.py](../03_Hashing/1074_Number_Of_Submatrices_That_Sum_To_Target.py) |
| 1160 | Find Words That Can Be Formed by Characters | Easy | Hashing (Frequency Counting) | `O(total chars)` | `O(1)` | Implemented & Tested | [1160_Find_Words_That_Can_Be_Formed_By_Characters.py](../03_Hashing/1160_Find_Words_That_Can_Be_Formed_By_Characters.py) |
| 1207 | Unique Number of Occurrences | Easy | Hashing (Hash Map + Hash Set) | `O(n)` | `O(n)` | Implemented & Tested | [1207_Unique_Number_Of_Occurrences.py](../03_Hashing/1207_Unique_Number_Of_Occurrences.py) |
| 1394 | Find Lucky Integer in an Array | Easy | Hashing (Frequency Counter) | `O(n)` | `O(n)` | Implemented & Tested | [1394_Find_Lucky_Integer_In_An_Array.py](../03_Hashing/1394_Find_Lucky_Integer_In_An_Array.py) |

## Two Pointers (`04_Two_Pointers/`) — 30 Problems
*Easy: 11 | Medium: 17 | Hard: 2*

| # | Title | Difficulty | Pattern | Time | Space | Status | Solution |
| :---: | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
| 5 | Longest Palindromic Substring | Medium | Two Pointers (Expand Around Center) | `O(n^2)` | `O(1)` | Implemented & Tested | [0005_Longest_Palindromic_Substring.py](../04_Two_Pointers/0005_Longest_Palindromic_Substring.py) |
| 11 | Container With Most Water | Medium | Two Pointers (Opposite Ends) | `O(n)` | `O(1)` | Implemented & Tested | [0011_Container_With_Most_Water.py](../04_Two_Pointers/0011_Container_With_Most_Water.py) |
| 15 | 3Sum | Medium | Two Pointers + Sorting | `O(n^2)` | `O(1) auxiliary` | Implemented & Tested | [0015_3Sum.py](../04_Two_Pointers/0015_3Sum.py) |
| 16 | 3Sum Closest | Medium | Two Pointers + Sorting | `O(n^2)` | `O(1) auxiliary` | Implemented & Tested | [0016_3Sum_Closest.py](../04_Two_Pointers/0016_3Sum_Closest.py) |
| 18 | 4Sum | Medium | Two Pointers + Sorting | `O(n^3)` | `O(1) auxiliary` | Implemented & Tested | [0018_4Sum.py](../04_Two_Pointers/0018_4Sum.py) |
| 28 | Find the Index of the First Occurrence in a String | Easy | Two Pointers / String Matching | `O(n * m)` | `O(1)` | Implemented & Tested | [0028_Find_The_Index_Of_The_First_Occurrence_In_A_String.py](../04_Two_Pointers/0028_Find_The_Index_Of_The_First_Occurrence_In_A_String.py) |
| 42 | Trapping Rain Water | Hard | Two Pointers (Opposite Ends) | `O(n)` | `O(1)` | Implemented & Tested | [0042_Trapping_Rain_Water.py](../04_Two_Pointers/0042_Trapping_Rain_Water.py) |
| 80 | Remove Duplicates from Sorted Array II | Medium | Two Pointers (In-Place) | `O(n)` | `O(1)` | Implemented & Tested | [0080_Remove_Duplicates_From_Sorted_Array_II.py](../04_Two_Pointers/0080_Remove_Duplicates_From_Sorted_Array_II.py) |
| 125 | Valid Palindrome | Easy | Two Pointers (Opposite Ends) | `O(n)` | `O(1)` | Implemented & Tested | [0125_Valid_Palindrome.py](../04_Two_Pointers/0125_Valid_Palindrome.py) |
| 151 | Reverse Words in a String | Medium | Two Pointers | `O(n)` | `O(n)` | Implemented & Tested | [0151_Reverse_Words_In_A_String.py](../04_Two_Pointers/0151_Reverse_Words_In_A_String.py) |
| 167 | Two Sum II - Input Array Is Sorted | Medium | Two Pointers (Opposite Ends) | `O(n)` | `O(1)` | Implemented & Tested | [0167_Two_Sum_II_Input_Array_Is_Sorted.py](../04_Two_Pointers/0167_Two_Sum_II_Input_Array_Is_Sorted.py) |
| 287 | Find the Duplicate Number | Medium | Two Pointers (Floyd's Cycle Detection) | `O(n)` | `O(1)` | Implemented & Tested | [0287_Find_The_Duplicate_Number.py](../04_Two_Pointers/0287_Find_The_Duplicate_Number.py) |
| 344 | Reverse String | Easy | Two Pointers (Opposite Ends) | `O(n)` | `O(1)` | Implemented & Tested | [0344_Reverse_String.py](../04_Two_Pointers/0344_Reverse_String.py) |
| 345 | Reverse Vowels of a String | Easy | Two Pointers (Opposite Ends) | `O(n)` | `O(n)` | Implemented & Tested | [0345_Reverse_Vowels_Of_A_String.py](../04_Two_Pointers/0345_Reverse_Vowels_Of_A_String.py) |
| 392 | Is Subsequence | Easy | Two Pointers | `O(n + m)` | `O(1)` | Implemented & Tested | [0392_Is_Subsequence.py](../04_Two_Pointers/0392_Is_Subsequence.py) |
| 443 | String Compression | Medium | Two Pointers (In-Place) | `O(n)` | `O(1)` | Implemented & Tested | [0443_String_Compression.py](../04_Two_Pointers/0443_String_Compression.py) |
| 455 | Assign Cookies | Easy | Two Pointers + Greedy Sorting | `O(n log n + m log m)` | `O(1) auxiliary` | Implemented & Tested | [0455_Assign_Cookies.py](../04_Two_Pointers/0455_Assign_Cookies.py) |
| 475 | Heaters | Medium | Two Pointers + Sorting | `O(n log n + m log m)` | `O(1) auxiliary` | Implemented & Tested | [0475_Heaters.py](../04_Two_Pointers/0475_Heaters.py) |
| 524 | Longest Word in Dictionary through Deleting | Medium | Two Pointers (Subsequence Matching) | `O(d * (n + k))` | `O(1) auxiliary` | Implemented & Tested | [0524_Longest_Word_In_Dictionary_Through_Deleting.py](../04_Two_Pointers/0524_Longest_Word_In_Dictionary_Through_Deleting.py) |
| 541 | Reverse String II | Easy | Two Pointers | `O(n)` | `O(n)` | Implemented & Tested | [0541_Reverse_String_II.py](../04_Two_Pointers/0541_Reverse_String_II.py) |
| 557 | Reverse Words in a String III | Easy | Two Pointers | `O(n)` | `O(n)` | Implemented & Tested | [0557_Reverse_Words_In_A_String_III.py](../04_Two_Pointers/0557_Reverse_Words_In_A_String_III.py) |
| 611 | Valid Triangle Number | Medium | Two Pointers + Sorting | `O(n^2)` | `O(1) auxiliary` | Implemented & Tested | [0611_Valid_Triangle_Number.py](../04_Two_Pointers/0611_Valid_Triangle_Number.py) |
| 633 | Sum of Square Numbers | Medium | Two Pointers (Search Space) | `O(sqrt(c))` | `O(1)` | Implemented & Tested | [0633_Sum_Of_Square_Numbers.py](../04_Two_Pointers/0633_Sum_Of_Square_Numbers.py) |
| 647 | Palindromic Substrings | Medium | Two Pointers (Expand Around Center) | `O(n^2)` | `O(1)` | Implemented & Tested | [0647_Palindromic_Substrings.py](../04_Two_Pointers/0647_Palindromic_Substrings.py) |
| 680 | Valid Palindrome II | Easy | Two Pointers (Opposite Ends) | `O(n)` | `O(1)` | Implemented & Tested | [0680_Valid_Palindrome_II.py](../04_Two_Pointers/0680_Valid_Palindrome_II.py) |
| 763 | Partition Labels | Medium | Two Pointers / Greedy Intervals | `O(n)` | `O(1)` | Implemented & Tested | [0763_Partition_Labels.py](../04_Two_Pointers/0763_Partition_Labels.py) |
| 844 | Backspace String Compare | Easy | Two Pointers (Reverse Scan) | `O(n + m)` | `O(1)` | Implemented & Tested | [0844_Backspace_String_Compare.py](../04_Two_Pointers/0844_Backspace_String_Compare.py) |
| 881 | Boats to Save People | Medium | Two Pointers + Greedy Sorting | `O(n log n)` | `O(1) auxiliary` | Implemented & Tested | [0881_Boats_To_Save_People.py](../04_Two_Pointers/0881_Boats_To_Save_People.py) |
| 905 | Sort Array By Parity | Easy | Two Pointers (Opposite Ends) | `O(n)` | `O(1) auxiliary` | Implemented & Tested | [0905_Sort_Array_By_Parity.py](../04_Two_Pointers/0905_Sort_Array_By_Parity.py) |
| 1793 | Maximum Score of a Good Subarray | Hard | Two Pointers (Greedy Expansion) | `O(n)` | `O(1)` | Implemented & Tested | [1793_Maximum_Score_Of_A_Good_Subarray.py](../04_Two_Pointers/1793_Maximum_Score_Of_A_Good_Subarray.py) |

## Sliding Window (`05_Sliding_Window/`) — 33 Problems
*Easy: 3 | Medium: 23 | Hard: 7*

| # | Title | Difficulty | Pattern | Time | Space | Status | Solution |
| :---: | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
| 3 | Longest Substring Without Repeating Characters | Medium | Sliding Window (Variable) + Hash Map | `O(n)` | `O(min(n, m))` | Implemented & Tested | [0003_Longest_Substring_Without_Repeating_Characters.py](../05_Sliding_Window/0003_Longest_Substring_Without_Repeating_Characters.py) |
| 30 | Substring with Concatenation of All Words | Hard | Sliding Window (Word-Length Offset) + Hash Map | `O(n * word_len)` | `O(k * word_len)` | Implemented & Tested | [0030_Substring_With_Concatenation_Of_All_Words.py](../05_Sliding_Window/0030_Substring_With_Concatenation_Of_All_Words.py) |
| 76 | Minimum Window Substring | Hard | Sliding Window (Variable) + Hash Map | `O(n + m)` | `O(m)` | Implemented & Tested | [0076_Minimum_Window_Substring.py](../05_Sliding_Window/0076_Minimum_Window_Substring.py) |
| 209 | Minimum Size Subarray Sum | Medium | Sliding Window (Variable) | `O(n)` | `O(1)` | Implemented & Tested | [0209_Minimum_Size_Subarray_Sum.py](../05_Sliding_Window/0209_Minimum_Size_Subarray_Sum.py) |
| 220 | Contains Duplicate III | Hard | Sliding Window + Bucketing | `O(n)` | `O(min(n, indexDiff))` | Implemented & Tested | [0220_Contains_Duplicate_III.py](../05_Sliding_Window/0220_Contains_Duplicate_III.py) |
| 239 | Sliding Window Maximum | Hard | Sliding Window + Monotonic Deque | `O(n)` | `O(k)` | Implemented & Tested | [0239_Sliding_Window_Maximum.py](../05_Sliding_Window/0239_Sliding_Window_Maximum.py) |
| 340 | Longest Substring with At Most K Distinct Characters | Medium | Sliding Window (Variable) + Hash Map | `O(n)` | `O(k)` | Implemented & Tested | [0340_Longest_Substring_With_At_Most_K_Distinct_Characters.py](../05_Sliding_Window/0340_Longest_Substring_With_At_Most_K_Distinct_Characters.py) |
| 424 | Longest Repeating Character Replacement | Medium | Sliding Window (Variable) + Frequency Array | `O(n)` | `O(1)` | Implemented & Tested | [0424_Longest_Repeating_Character_Replacement.py](../05_Sliding_Window/0424_Longest_Repeating_Character_Replacement.py) |
| 438 | Find All Anagrams in a String | Medium | Sliding Window (Fixed) + Frequency Array | `O(n)` | `O(1)` | Implemented & Tested | [0438_Find_All_Anagrams_In_A_String.py](../05_Sliding_Window/0438_Find_All_Anagrams_In_A_String.py) |
| 567 | Permutation in String | Medium | Sliding Window (Fixed) + Frequency Array | `O(n)` | `O(1)` | Implemented & Tested | [0567_Permutation_In_String.py](../05_Sliding_Window/0567_Permutation_In_String.py) |
| 643 | Maximum Average Subarray I | Easy | Sliding Window (Fixed) | `O(n)` | `O(1)` | Implemented & Tested | [0643_Maximum_Average_Subarray_I.py](../05_Sliding_Window/0643_Maximum_Average_Subarray_I.py) |
| 713 | Subarray Product Less Than K | Medium | Sliding Window (Variable) | `O(n)` | `O(1)` | Implemented & Tested | [0713_Subarray_Product_Less_Than_K.py](../05_Sliding_Window/0713_Subarray_Product_Less_Than_K.py) |
| 904 | Fruit Into Baskets | Medium | Sliding Window (At Most 2 Distinct) | `O(n)` | `O(1)` | Implemented & Tested | [0904_Fruit_Into_Baskets.py](../05_Sliding_Window/0904_Fruit_Into_Baskets.py) |
| 930 | Binary Subarrays With Sum | Medium | Sliding Window (At Most Goal Difference) | `O(n)` | `O(1)` | Implemented & Tested | [0930_Binary_Subarrays_With_Sum.py](../05_Sliding_Window/0930_Binary_Subarrays_With_Sum.py) |
| 992 | Subarrays with K Different Integers | Hard | Sliding Window (At Most K Difference) | `O(n)` | `O(n)` | Implemented & Tested | [0992_Subarrays_With_K_Different_Integers.py](../05_Sliding_Window/0992_Subarrays_With_K_Different_Integers.py) |
| 1004 | Max Consecutive Ones III | Medium | Sliding Window (Variable) | `O(n)` | `O(1)` | Implemented & Tested | [1004_Max_Consecutive_Ones_III.py](../05_Sliding_Window/1004_Max_Consecutive_Ones_III.py) |
| 1052 | Grumpy Bookstore Owner | Medium | Sliding Window (Fixed) | `O(n)` | `O(1)` | Implemented & Tested | [1052_Grumpy_Bookstore_Owner.py](../05_Sliding_Window/1052_Grumpy_Bookstore_Owner.py) |
| 1208 | Get Equal Substrings Within Budget | Medium | Sliding Window (Variable) | `O(n)` | `O(1)` | Implemented & Tested | [1208_Get_Equal_Substrings_Within_Budget.py](../05_Sliding_Window/1208_Get_Equal_Substrings_Within_Budget.py) |
| 1248 | Count Number of Nice Subarrays | Medium | Sliding Window (At Most K Difference) | `O(n)` | `O(1)` | Implemented & Tested | [1248_Count_Number_Of_Nice_Subarrays.py](../05_Sliding_Window/1248_Count_Number_Of_Nice_Subarrays.py) |
| 1343 | Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold | Medium | Sliding Window (Fixed) | `O(n)` | `O(1)` | Implemented & Tested | [1343_Number_Of_Sub_Arrays_Of_Size_K_And_Average_Greater_Than_Or_Equal_To_Threshold.py](../05_Sliding_Window/1343_Number_Of_Sub_Arrays_Of_Size_K_And_Average_Greater_Than_Or_Equal_To_Threshold.py) |
| 1358 | Number of Substrings Containing All Three Characters | Medium | Sliding Window (Variable) | `O(n)` | `O(1)` | Implemented & Tested | [1358_Number_Of_Substrings_Containing_All_Three_Characters.py](../05_Sliding_Window/1358_Number_Of_Substrings_Containing_All_Three_Characters.py) |
| 1423 | Maximum Points You Can Obtain from Cards | Medium | Sliding Window (Fixed Complement) | `O(n)` | `O(1)` | Implemented & Tested | [1423_Maximum_Points_You_Can_Obtain_From_Cards.py](../05_Sliding_Window/1423_Maximum_Points_You_Can_Obtain_From_Cards.py) |
| 1438 | Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit | Medium | Sliding Window + Monotonic Deques | `O(n)` | `O(n)` | Implemented & Tested | [1438_Longest_Continuous_Subarray_With_Absolute_Diff_Less_Than_Or_Equal_To_Limit.py](../05_Sliding_Window/1438_Longest_Continuous_Subarray_With_Absolute_Diff_Less_Than_Or_Equal_To_Limit.py) |
| 1456 | Maximum Number of Vowels in a Substring of Given Length | Medium | Sliding Window (Fixed) | `O(n)` | `O(1)` | Implemented & Tested | [1456_Maximum_Number_Of_Vowels_In_A_Substring_Of_Given_Length.py](../05_Sliding_Window/1456_Maximum_Number_Of_Vowels_In_A_Substring_Of_Given_Length.py) |
| 1493 | Longest Subarray of 1's After Deleting One Element | Medium | Sliding Window (Variable) | `O(n)` | `O(1)` | Implemented & Tested | [1493_Longest_Subarray_Of_1s_After_Deleting_One_Element.py](../05_Sliding_Window/1493_Longest_Subarray_Of_1s_After_Deleting_One_Element.py) |
| 1658 | Minimum Operations to Reduce X to Zero | Medium | Sliding Window (Complement Target Sum) | `O(n)` | `O(1)` | Implemented & Tested | [1658_Minimum_Operations_To_Reduce_X_To_Zero.py](../05_Sliding_Window/1658_Minimum_Operations_To_Reduce_X_To_Zero.py) |
| 1695 | Maximum Erasure Value | Medium | Sliding Window (Variable) + Hash Set | `O(n)` | `O(n)` | Implemented & Tested | [1695_Maximum_Erasure_Value.py](../05_Sliding_Window/1695_Maximum_Erasure_Value.py) |
| 1838 | Frequency of the Most Frequent Element | Medium | Sliding Window (Variable) + Sorting | `O(n log n)` | `O(1) auxiliary` | Implemented & Tested | [1838_Frequency_Of_The_Most_Frequent_Element.py](../05_Sliding_Window/1838_Frequency_Of_The_Most_Frequent_Element.py) |
| 1876 | Substrings of Size Three with Distinct Characters | Easy | Sliding Window (Fixed) | `O(n)` | `O(1)` | Implemented & Tested | [1876_Substrings_Of_Size_Three_With_Distinct_Characters.py](../05_Sliding_Window/1876_Substrings_Of_Size_Three_With_Distinct_Characters.py) |
| 2269 | Find the K-Beauty of a Number | Easy | Sliding Window (Fixed) | `O(d)` | `O(d)` | Implemented & Tested | [2269_Find_The_K_Beauty_Of_A_Number.py](../05_Sliding_Window/2269_Find_The_K_Beauty_Of_A_Number.py) |
| 2302 | Count Subarrays With Score Less Than K | Hard | Sliding Window (Variable) | `O(n)` | `O(1)` | Implemented & Tested | [2302_Count_Subarrays_With_Score_Less_Than_K.py](../05_Sliding_Window/2302_Count_Subarrays_With_Score_Less_Than_K.py) |
| 2444 | Count Subarrays With Fixed Bounds | Hard | Sliding Window (Last-Seen Bound Tracking) | `O(n)` | `O(1)` | Implemented & Tested | [2444_Count_Subarrays_With_Fixed_Bounds.py](../05_Sliding_Window/2444_Count_Subarrays_With_Fixed_Bounds.py) |
| 2958 | Length of Longest Subarray With at Most K Frequency | Medium | Sliding Window (Variable) + Hash Map | `O(n)` | `O(n)` | Implemented & Tested | [2958_Length_Of_Longest_Subarray_With_At_Most_K_Frequency.py](../05_Sliding_Window/2958_Length_Of_Longest_Subarray_With_At_Most_K_Frequency.py) |

## Binary Search (`06_Binary_Search/`) — 36 Problems
*Easy: 11 | Medium: 21 | Hard: 4*

| # | Title | Difficulty | Pattern | Time | Space | Status | Solution |
| :---: | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
| 4 | Median of Two Sorted Arrays | Hard | Binary Search (Partitioning) | `O(log(min(m, n)))` | `O(1)` | Implemented & Tested | [0004_Median_Of_Two_Sorted_Arrays.py](../06_Binary_Search/0004_Median_Of_Two_Sorted_Arrays.py) |
| 33 | Search in Rotated Sorted Array | Medium | Binary Search (Rotated Array) | `O(log n)` | `O(1)` | Implemented & Tested | [0033_Search_In_Rotated_Sorted_Array.py](../06_Binary_Search/0033_Search_In_Rotated_Sorted_Array.py) |
| 34 | Find First and Last Position of Element in Sorted Array | Medium | Binary Search (Lower and Upper Bounds) | `O(log n)` | `O(1)` | Implemented & Tested | [0034_Find_First_And_Last_Position_Of_Element_In_Sorted_Array.py](../06_Binary_Search/0034_Find_First_And_Last_Position_Of_Element_In_Sorted_Array.py) |
| 35 | Search Insert Position | Easy | Binary Search (Lower Bound) | `O(log n)` | `O(1)` | Implemented & Tested | [0035_Search_Insert_Position.py](../06_Binary_Search/0035_Search_Insert_Position.py) |
| 69 | Sqrt(x) | Easy | Binary Search on Answer | `O(log x)` | `O(1)` | Implemented & Tested | [0069_Sqrt_X.py](../06_Binary_Search/0069_Sqrt_X.py) |
| 74 | Search a 2D Matrix | Medium | Binary Search (2D Matrix) | `O(log(m * n))` | `O(1)` | Implemented & Tested | [0074_Search_A_2D_Matrix.py](../06_Binary_Search/0074_Search_A_2D_Matrix.py) |
| 81 | Search in Rotated Sorted Array II | Medium | Binary Search (Rotated Array with Duplicates) | `O(log n) average, O(n) worst` | `O(1)` | Implemented & Tested | [0081_Search_In_Rotated_Sorted_Array_II.py](../06_Binary_Search/0081_Search_In_Rotated_Sorted_Array_II.py) |
| 153 | Find Minimum in Rotated Sorted Array | Medium | Binary Search (Rotated Array) | `O(log n)` | `O(1)` | Implemented & Tested | [0153_Find_Minimum_In_Rotated_Sorted_Array.py](../06_Binary_Search/0153_Find_Minimum_In_Rotated_Sorted_Array.py) |
| 154 | Find Minimum in Rotated Sorted Array II | Hard | Binary Search (Rotated Array with Duplicates) | `O(log n) average, O(n) worst` | `O(1)` | Implemented & Tested | [0154_Find_Minimum_In_Rotated_Sorted_Array_II.py](../06_Binary_Search/0154_Find_Minimum_In_Rotated_Sorted_Array_II.py) |
| 162 | Find Peak Element | Medium | Binary Search (Peak Finding) | `O(log n)` | `O(1)` | Implemented & Tested | [0162_Find_Peak_Element.py](../06_Binary_Search/0162_Find_Peak_Element.py) |
| 275 | H-Index II | Medium | Binary Search (Index Offset) | `O(log n)` | `O(1)` | Implemented & Tested | [0275_H_Index_II.py](../06_Binary_Search/0275_H_Index_II.py) |
| 278 | First Bad Version | Easy | Binary Search (Lower Bound) | `O(log n)` | `O(1)` | Implemented & Tested | [0278_First_Bad_Version.py](../06_Binary_Search/0278_First_Bad_Version.py) |
| 367 | Valid Perfect Square | Easy | Binary Search on Answer | `O(log num)` | `O(1)` | Implemented & Tested | [0367_Valid_Perfect_Square.py](../06_Binary_Search/0367_Valid_Perfect_Square.py) |
| 374 | Guess Number Higher or Lower | Easy | Binary Search (Classic) | `O(log n)` | `O(1)` | Implemented & Tested | [0374_Guess_Number_Higher_Or_Lower.py](../06_Binary_Search/0374_Guess_Number_Higher_Or_Lower.py) |
| 410 | Split Array Largest Sum | Hard | Binary Search on Answer | `O(n log(sum(nums)))` | `O(1)` | Implemented & Tested | [0410_Split_Array_Largest_Sum.py](../06_Binary_Search/0410_Split_Array_Largest_Sum.py) |
| 441 | Arranging Coins | Easy | Binary Search on Answer | `O(log n)` | `O(1)` | Implemented & Tested | [0441_Arranging_Coins.py](../06_Binary_Search/0441_Arranging_Coins.py) |
| 540 | Single Element in a Sorted Array | Medium | Binary Search (Index Parity) | `O(log n)` | `O(1)` | Implemented & Tested | [0540_Single_Element_In_A_Sorted_Array.py](../06_Binary_Search/0540_Single_Element_In_A_Sorted_Array.py) |
| 658 | Find K Closest Elements | Medium | Binary Search (Window Start Search) | `O(log(n - k) + k)` | `O(1) auxiliary` | Implemented & Tested | [0658_Find_K_Closest_Elements.py](../06_Binary_Search/0658_Find_K_Closest_Elements.py) |
