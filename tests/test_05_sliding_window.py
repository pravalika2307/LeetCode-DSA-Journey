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



if __name__ == "__main__":
    unittest.main()
