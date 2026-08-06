import unittest

from tests.helpers import ListNode, from_linked_list, load_solution, to_linked_list


class TestTwoPointers(unittest.TestCase):
    def test_0005(self):
        mod = load_solution("04_Two_Pointers/0005_Longest_Palindromic_Substring.py")
        sol = mod.Solution()
        self.assertIn(sol.longestPalindrome("babad"), ("bab", "aba"))

    def test_0011(self):
        mod = load_solution("04_Two_Pointers/0011_Container_With_Most_Water.py")
        sol = mod.Solution()
        self.assertEqual(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_0015(self):
        mod = load_solution("04_Two_Pointers/0015_3Sum.py")
        sol = mod.Solution()
        self.assertEqual(sol.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])



if __name__ == "__main__":
    unittest.main()
