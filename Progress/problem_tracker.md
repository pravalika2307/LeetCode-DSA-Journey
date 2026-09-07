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
