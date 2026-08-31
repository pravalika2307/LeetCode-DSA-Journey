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

    def test_0287(self):
        mod = load_solution("04_Two_Pointers/0287_Find_The_Duplicate_Number.py")
        sol = mod.Solution()
        self.assertEqual(sol.findDuplicate([1, 3, 4, 2, 2]), 2)

    def test_0344(self):
        mod = load_solution("04_Two_Pointers/0344_Reverse_String.py")
        sol = mod.Solution()
        s = list("hello"); sol.reverseString(s); self.assertEqual(s, list("olleh"))

    def test_0345(self):
        mod = load_solution("04_Two_Pointers/0345_Reverse_Vowels_Of_A_String.py")
        sol = mod.Solution()
        self.assertEqual(sol.reverseVowels("hello"), "holle")

    def test_0392(self):
        mod = load_solution("04_Two_Pointers/0392_Is_Subsequence.py")
        sol = mod.Solution()
        self.assertTrue(sol.isSubsequence("abc", "ahbgdc"))

    def test_0443(self):
        mod = load_solution("04_Two_Pointers/0443_String_Compression.py")
        sol = mod.Solution()
        ch = ["a", "a", "b", "b", "c", "c", "c"]; k = sol.compress(ch); self.assertEqual((k, ch[:k]), (6, ["a", "2", "b", "2", "c", "3"]))

    def test_0455(self):
        mod = load_solution("04_Two_Pointers/0455_Assign_Cookies.py")
        sol = mod.Solution()
        self.assertEqual(sol.findContentChildren([1, 2, 3], [1, 1]), 1)

    def test_0475(self):
        mod = load_solution("04_Two_Pointers/0475_Heaters.py")
        sol = mod.Solution()
        self.assertEqual(sol.findRadius([1, 2, 3], [2]), 1)

    def test_0524(self):
        mod = load_solution("04_Two_Pointers/0524_Longest_Word_In_Dictionary_Through_Deleting.py")
        sol = mod.Solution()
        self.assertEqual(sol.findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]), "apple")

    def test_0541(self):
        mod = load_solution("04_Two_Pointers/0541_Reverse_String_II.py")
        sol = mod.Solution()
        self.assertEqual(sol.reverseStr("abcdefg", 2), "bacdfeg")

    def test_0557(self):
        mod = load_solution("04_Two_Pointers/0557_Reverse_Words_In_A_String_III.py")
        sol = mod.Solution()
        self.assertEqual(sol.reverseWords("Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc")

    def test_0611(self):
        mod = load_solution("04_Two_Pointers/0611_Valid_Triangle_Number.py")
        sol = mod.Solution()
        self.assertEqual(sol.triangleNumber([2, 2, 3, 4]), 3)

    def test_0633(self):
        mod = load_solution("04_Two_Pointers/0633_Sum_Of_Square_Numbers.py")
        sol = mod.Solution()
        self.assertTrue(sol.judgeSquareSum(5)); self.assertFalse(sol.judgeSquareSum(3))

    def test_0647(self):
        mod = load_solution("04_Two_Pointers/0647_Palindromic_Substrings.py")
        sol = mod.Solution()
        self.assertEqual(sol.countSubstrings("aaa"), 6)

    def test_0680(self):
        mod = load_solution("04_Two_Pointers/0680_Valid_Palindrome_II.py")
        sol = mod.Solution()
        self.assertTrue(sol.validPalindrome("abca")); self.assertFalse(sol.validPalindrome("abc"))

    def test_0763(self):
        mod = load_solution("04_Two_Pointers/0763_Partition_Labels.py")
        sol = mod.Solution()
        self.assertEqual(sol.partitionLabels("ababcbacadefegdehijhklij"), [9, 7, 8])

    def test_0844(self):
        mod = load_solution("04_Two_Pointers/0844_Backspace_String_Compare.py")
        sol = mod.Solution()
        self.assertTrue(sol.backspaceCompare("ab#c", "ad#c"))

    def test_0881(self):
        mod = load_solution("04_Two_Pointers/0881_Boats_To_Save_People.py")
        sol = mod.Solution()
        self.assertEqual(sol.numRescueBoats([3, 2, 2, 1], 3), 3)

    def test_0905(self):
        mod = load_solution("04_Two_Pointers/0905_Sort_Array_By_Parity.py")
        sol = mod.Solution()
        res = sol.sortArrayByParity([3, 1, 2, 4]); self.assertTrue(all(x % 2 == 0 for x in res[:2]) and all(x % 2 == 1 for x in res[2:]))



if __name__ == "__main__":
    unittest.main()
