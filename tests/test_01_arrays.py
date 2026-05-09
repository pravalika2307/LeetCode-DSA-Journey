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

    def test_0027(self):
        mod = load_solution("01_Arrays/0027_Remove_Element.py")
        sol = mod.Solution()
        a = [3, 2, 2, 3]; k = sol.removeElement(a, 3); self.assertEqual((k, sorted(a[:k])), (2, [2, 2]))

    def test_0031(self):
        mod = load_solution("01_Arrays/0031_Next_Permutation.py")
        sol = mod.Solution()
        a = [1, 2, 3]; sol.nextPermutation(a); self.assertEqual(a, [1, 3, 2])

    def test_0041(self):
        mod = load_solution("01_Arrays/0041_First_Missing_Positive.py")
        sol = mod.Solution()
        self.assertEqual(sol.firstMissingPositive([3, 4, -1, 1]), 2); self.assertEqual(sol.firstMissingPositive([1, 2, 0]), 3)



if __name__ == "__main__":
    unittest.main()
