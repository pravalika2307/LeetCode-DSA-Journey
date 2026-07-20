import unittest

from tests.helpers import ListNode, from_linked_list, load_solution, to_linked_list


class TestHashing(unittest.TestCase):
    def test_0036(self):
        mod = load_solution("03_Hashing/0036_Valid_Sudoku.py")
        sol = mod.Solution()
        board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]; self.assertTrue(sol.isValidSudoku(board))

    def test_0049(self):
        mod = load_solution("03_Hashing/0049_Group_Anagrams.py")
        sol = mod.Solution()
        groups = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]); self.assertEqual(sorted(sorted(g) for g in groups), [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]])

    def test_0128(self):
        mod = load_solution("03_Hashing/0128_Longest_Consecutive_Sequence.py")
        sol = mod.Solution()
        self.assertEqual(sol.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_0136(self):
        mod = load_solution("03_Hashing/0136_Single_Number.py")
        sol = mod.Solution()
        self.assertEqual(sol.singleNumber([4, 1, 2, 1, 2]), 4)

    def test_0149(self):
        mod = load_solution("03_Hashing/0149_Max_Points_On_A_Line.py")
        sol = mod.Solution()
        self.assertEqual(sol.maxPoints([[1, 1], [2, 2], [3, 3]]), 3)

    def test_0187(self):
        mod = load_solution("03_Hashing/0187_Repeated_DNA_Sequences.py")
        sol = mod.Solution()
        self.assertEqual(sorted(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")), ["AAAAACCCCC", "CCCCCAAAAA"])

    def test_0202(self):
        mod = load_solution("03_Hashing/0202_Happy_Number.py")
        sol = mod.Solution()
        self.assertTrue(sol.isHappy(19)); self.assertFalse(sol.isHappy(2))

    def test_0205(self):
        mod = load_solution("03_Hashing/0205_Isomorphic_Strings.py")
        sol = mod.Solution()
        self.assertTrue(sol.isIsomorphic("egg", "add")); self.assertFalse(sol.isIsomorphic("foo", "bar"))

    def test_0219(self):
        mod = load_solution("03_Hashing/0219_Contains_Duplicate_II.py")
        sol = mod.Solution()
        self.assertTrue(sol.containsNearbyDuplicate([1, 2, 3, 1], 3)); self.assertFalse(sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))

    def test_0242(self):
        mod = load_solution("03_Hashing/0242_Valid_Anagram.py")
        sol = mod.Solution()
        self.assertTrue(sol.isAnagram("anagram", "nagaram"))

    def test_0290(self):
        mod = load_solution("03_Hashing/0290_Word_Pattern.py")
        sol = mod.Solution()
        self.assertTrue(sol.wordPattern("abba", "dog cat cat dog"))

    def test_0299(self):
        mod = load_solution("03_Hashing/0299_Bulls_And_Cows.py")
        sol = mod.Solution()
        self.assertEqual(sol.getHint("1807", "7810"), "1A3B")

    def test_0349(self):
        mod = load_solution("03_Hashing/0349_Intersection_Of_Two_Arrays.py")
        sol = mod.Solution()
        self.assertEqual(sorted(sol.intersection([1, 2, 2, 1], [2, 2])), [2])

    def test_0350(self):
        mod = load_solution("03_Hashing/0350_Intersection_Of_Two_Arrays_II.py")
        sol = mod.Solution()
        self.assertEqual(sorted(sol.intersect([1, 2, 2, 1], [2, 2])), [2, 2])

    def test_0383(self):
        mod = load_solution("03_Hashing/0383_Ransom_Note.py")
        sol = mod.Solution()
        self.assertTrue(sol.canConstruct("aa", "aab"))

    def test_0387(self):
        mod = load_solution("03_Hashing/0387_First_Unique_Character_In_A_String.py")
        sol = mod.Solution()
        self.assertEqual(sol.firstUniqChar("loveleetcode"), 2)

    def test_0389(self):
        mod = load_solution("03_Hashing/0389_Find_The_Difference.py")
        sol = mod.Solution()
        self.assertEqual(sol.findTheDifference("abcd", "abcde"), "e")

    def test_0409(self):
        mod = load_solution("03_Hashing/0409_Longest_Palindrome.py")
        sol = mod.Solution()
        self.assertEqual(sol.longestPalindrome("abccccdd"), 7)

    def test_0447(self):
        mod = load_solution("03_Hashing/0447_Number_Of_Boomerangs.py")
        sol = mod.Solution()
        self.assertEqual(sol.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]), 2)

    def test_0451(self):
        mod = load_solution("03_Hashing/0451_Sort_Characters_By_Frequency.py")
        sol = mod.Solution()
        self.assertIn(sol.frequencySort("tree"), ("eert", "eetr"))

    def test_0454(self):
        mod = load_solution("03_Hashing/0454_4Sum_II.py")
        sol = mod.Solution()
        self.assertEqual(sol.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]), 2)

    def test_0500(self):
        mod = load_solution("03_Hashing/0500_Keyboard_Row.py")
        sol = mod.Solution()
        self.assertEqual(sol.findWords(["Hello", "Alaska", "Dad", "Peace"]), ["Alaska", "Dad"])

    def test_0523(self):
        mod = load_solution("03_Hashing/0523_Continuous_Subarray_Sum.py")
        sol = mod.Solution()
        self.assertTrue(sol.checkSubarraySum([23, 2, 4, 6, 7], 6))

    def test_0525(self):
        mod = load_solution("03_Hashing/0525_Contiguous_Array.py")
        sol = mod.Solution()
        self.assertEqual(sol.findMaxLength([0, 1, 0]), 2)

    def test_0532(self):
        mod = load_solution("03_Hashing/0532_K_Diff_Pairs_In_An_Array.py")
        sol = mod.Solution()
        self.assertEqual(sol.findPairs([3, 1, 4, 1, 5], 2), 2)



if __name__ == "__main__":
    unittest.main()
