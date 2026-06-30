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



if __name__ == "__main__":
    unittest.main()
