import unittest

from tests.helpers import ListNode, from_linked_list, load_solution, to_linked_list


class TestSlidingWindow(unittest.TestCase):
    def test_0003(self):
        mod = load_solution("05_Sliding_Window/0003_Longest_Substring_Without_Repeating_Characters.py")
        sol = mod.Solution()
        self.assertEqual(sol.lengthOfLongestSubstring("abcabcbb"), 3)



if __name__ == "__main__":
    unittest.main()
