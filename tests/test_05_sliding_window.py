import unittest

from tests.helpers import ListNode, from_linked_list, load_solution, to_linked_list


class TestSlidingWindow(unittest.TestCase):
    def test_0003(self):
        mod = load_solution("05_Sliding_Window/0003_Longest_Substring_Without_Repeating_Characters.py")
        sol = mod.Solution()
        self.assertEqual(sol.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_0030(self):
        mod = load_solution("05_Sliding_Window/0030_Substring_With_Concatenation_Of_All_Words.py")
        sol = mod.Solution()
        self.assertEqual(sorted(sol.findSubstring("barfoothefoobarman", ["foo", "bar"])), [0, 9])

    def test_0076(self):
        mod = load_solution("05_Sliding_Window/0076_Minimum_Window_Substring.py")
        sol = mod.Solution()
        self.assertEqual(sol.minWindow("ADOBECODEBANC", "ABC"), "BANC")

    def test_0209(self):
        mod = load_solution("05_Sliding_Window/0209_Minimum_Size_Subarray_Sum.py")
        sol = mod.Solution()
        self.assertEqual(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]), 2)

    def test_0220(self):
        mod = load_solution("05_Sliding_Window/0220_Contains_Duplicate_III.py")
        sol = mod.Solution()
        self.assertTrue(sol.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)); self.assertFalse(sol.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))

    def test_0239(self):
        mod = load_solution("05_Sliding_Window/0239_Sliding_Window_Maximum.py")
        sol = mod.Solution()
        self.assertEqual(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])

    def test_0340(self):
        mod = load_solution("05_Sliding_Window/0340_Longest_Substring_With_At_Most_K_Distinct_Characters.py")
        sol = mod.Solution()
        self.assertEqual(sol.lengthOfLongestSubstringKDistinct("eceba", 2), 3)

    def test_0424(self):
        mod = load_solution("05_Sliding_Window/0424_Longest_Repeating_Character_Replacement.py")
        sol = mod.Solution()
        self.assertEqual(sol.characterReplacement("AABABBA", 1), 4)

    def test_0438(self):
        mod = load_solution("05_Sliding_Window/0438_Find_All_Anagrams_In_A_String.py")
        sol = mod.Solution()
        self.assertEqual(sol.findAnagrams("cbaebabacd", "abc"), [0, 6])

    def test_0567(self):
        mod = load_solution("05_Sliding_Window/0567_Permutation_In_String.py")
        sol = mod.Solution()
        self.assertTrue(sol.checkInclusion("ab", "eidbaooo"))

    def test_0643(self):
        mod = load_solution("05_Sliding_Window/0643_Maximum_Average_Subarray_I.py")
        sol = mod.Solution()
        self.assertEqual(sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4), 12.75)

    def test_0713(self):
        mod = load_solution("05_Sliding_Window/0713_Subarray_Product_Less_Than_K.py")
        sol = mod.Solution()
        self.assertEqual(sol.numSubarrayProductLessThanK([10, 5, 2, 6], 100), 8)

    def test_0904(self):
        mod = load_solution("05_Sliding_Window/0904_Fruit_Into_Baskets.py")
        sol = mod.Solution()
        self.assertEqual(sol.totalFruit([1, 2, 3, 2, 2]), 4)

    def test_0930(self):
        mod = load_solution("05_Sliding_Window/0930_Binary_Subarrays_With_Sum.py")
        sol = mod.Solution()
        self.assertEqual(sol.numSubarraysWithSum([1, 0, 1, 0, 1], 2), 4)

    def test_0992(self):
        mod = load_solution("05_Sliding_Window/0992_Subarrays_With_K_Different_Integers.py")
        sol = mod.Solution()
        self.assertEqual(sol.subarraysWithKDistinct([1, 2, 1, 2, 3], 2), 7)

    def test_1004(self):
        mod = load_solution("05_Sliding_Window/1004_Max_Consecutive_Ones_III.py")
        sol = mod.Solution()
        self.assertEqual(sol.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6)

    def test_1052(self):
        mod = load_solution("05_Sliding_Window/1052_Grumpy_Bookstore_Owner.py")
        sol = mod.Solution()
        self.assertEqual(sol.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3), 16)

    def test_1208(self):
        mod = load_solution("05_Sliding_Window/1208_Get_Equal_Substrings_Within_Budget.py")
        sol = mod.Solution()
        self.assertEqual(sol.equalSubstring("abcd", "bcdf", 3), 3)

    def test_1248(self):
        mod = load_solution("05_Sliding_Window/1248_Count_Number_Of_Nice_Subarrays.py")
        sol = mod.Solution()
        self.assertEqual(sol.numberOfSubarrays([1, 1, 2, 1, 1], 3), 2)

    def test_1343(self):
        mod = load_solution("05_Sliding_Window/1343_Number_Of_Sub_Arrays_Of_Size_K_And_Average_Greater_Than_Or_Equal_To_Threshold.py")
        sol = mod.Solution()
        self.assertEqual(sol.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4), 3)

    def test_1358(self):
        mod = load_solution("05_Sliding_Window/1358_Number_Of_Substrings_Containing_All_Three_Characters.py")
        sol = mod.Solution()
        self.assertEqual(sol.numberOfSubstrings("abcabc"), 10)

    def test_1423(self):
        mod = load_solution("05_Sliding_Window/1423_Maximum_Points_You_Can_Obtain_From_Cards.py")
        sol = mod.Solution()
        self.assertEqual(sol.maxScore([1, 2, 3, 4, 5, 6, 1], 3), 12)

    def test_1438(self):
        mod = load_solution("05_Sliding_Window/1438_Longest_Continuous_Subarray_With_Absolute_Diff_Less_Than_Or_Equal_To_Limit.py")
        sol = mod.Solution()
        self.assertEqual(sol.longestSubarray([8, 2, 4, 7], 4), 2)

    def test_1456(self):
        mod = load_solution("05_Sliding_Window/1456_Maximum_Number_Of_Vowels_In_A_Substring_Of_Given_Length.py")
        sol = mod.Solution()
        self.assertEqual(sol.maxVowels("abciiidef", 3), 3)

    def test_1493(self):
        mod = load_solution("05_Sliding_Window/1493_Longest_Subarray_Of_1s_After_Deleting_One_Element.py")
        sol = mod.Solution()
        self.assertEqual(sol.longestSubarray([1, 1, 0, 1]), 3); self.assertEqual(sol.longestSubarray([1, 1, 1]), 2)

    def test_1658(self):
        mod = load_solution("05_Sliding_Window/1658_Minimum_Operations_To_Reduce_X_To_Zero.py")
        sol = mod.Solution()
        self.assertEqual(sol.minOperations([1, 1, 4, 2, 3], 5), 2)

    def test_1695(self):
        mod = load_solution("05_Sliding_Window/1695_Maximum_Erasure_Value.py")
        sol = mod.Solution()
        self.assertEqual(sol.maximumUniqueSubarray([4, 2, 4, 5, 6]), 17)

    def test_1838(self):
        mod = load_solution("05_Sliding_Window/1838_Frequency_Of_The_Most_Frequent_Element.py")
        sol = mod.Solution()
        self.assertEqual(sol.maxFrequency([1, 2, 4], 5), 3)



if __name__ == "__main__":
    unittest.main()
