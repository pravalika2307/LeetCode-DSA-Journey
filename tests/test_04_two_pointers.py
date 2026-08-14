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

    def test_0080(self):
        mod = load_solution("04_Two_Pointers/0080_Remove_Duplicates_From_Sorted_Array_II.py")
        sol = mod.Solution()
        a = [1, 1, 1, 2, 2, 3]; k = sol.removeDuplicates(a); self.assertEqual((k, a[:k]), (5, [1, 1, 2, 2, 3]))

    def test_0125(self):
        mod = load_solution("04_Two_Pointers/0125_Valid_Palindrome.py")
        sol = mod.Solution()
        self.assertTrue(sol.isPalindrome("A man, a plan, a canal: Panama"))

    def test_0151(self):
        mod = load_solution("04_Two_Pointers/0151_Reverse_Words_In_A_String.py")
        sol = mod.Solution()
        self.assertEqual(sol.reverseWords("  hello world  "), "world hello")

    def test_0167(self):
        mod = load_solution("04_Two_Pointers/0167_Two_Sum_II_Input_Array_Is_Sorted.py")
        sol = mod.Solution()
        self.assertEqual(sol.twoSum([2, 7, 11, 15], 9), [1, 2])



if __name__ == "__main__":
    unittest.main()
