import unittest

from tests.helpers import ListNode, from_linked_list, load_solution, to_linked_list


class TestTwoPointers(unittest.TestCase):
    def test_0005(self):
        mod = load_solution("04_Two_Pointers/0005_Longest_Palindromic_Substring.py")
        sol = mod.Solution()
        self.assertIn(sol.longestPalindrome("babad"), ("bab", "aba"))



if __name__ == "__main__":
    unittest.main()
