import unittest

from tests.helpers import ListNode, from_linked_list, load_solution, to_linked_list


class TestArrays(unittest.TestCase):
    def test_0001(self):
        mod = load_solution("01_Arrays/0001_Two_Sum.py")
        sol = mod.Solution()
        self.assertEqual(sol.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_0026(self):
        mod = load_solution("01_Arrays/0026_Remove_Duplicates_From_Sorted_Array.py")
        sol = mod.Solution()
        a = [1, 1, 2]; k = sol.removeDuplicates(a); self.assertEqual((k, a[:k]), (2, [1, 2]))



if __name__ == "__main__":
    unittest.main()
