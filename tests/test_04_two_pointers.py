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

    def test_0016(self):
        mod = load_solution("04_Two_Pointers/0016_3Sum_Closest.py")
        sol = mod.Solution()
        self.assertEqual(sol.threeSumClosest([-1, 2, 1, -4], 1), 2)

    def test_0018(self):
        mod = load_solution("04_Two_Pointers/0018_4Sum.py")
        sol = mod.Solution()
        self.assertEqual(sol.fourSum([1, 0, -1, 0, -2, 2], 0), [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])

    def test_0028(self):
        mod = load_solution("04_Two_Pointers/0028_Find_The_Index_Of_The_First_Occurrence_In_A_String.py")
        sol = mod.Solution()
        self.assertEqual(sol.strStr("sadbutsad", "sad"), 0); self.assertEqual(sol.strStr("leetcode", "leeto"), -1)

    def test_0042(self):
        mod = load_solution("04_Two_Pointers/0042_Trapping_Rain_Water.py")
        sol = mod.Solution()
        self.assertEqual(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)



if __name__ == "__main__":
    unittest.main()
