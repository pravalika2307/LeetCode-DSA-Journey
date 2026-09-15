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



if __name__ == "__main__":
    unittest.main()
