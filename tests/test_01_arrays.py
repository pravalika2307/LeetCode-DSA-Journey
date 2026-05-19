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

    def test_0048(self):
        mod = load_solution("01_Arrays/0048_Rotate_Image.py")
        sol = mod.Solution()
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]; sol.rotate(m); self.assertEqual(m, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    def test_0053(self):
        mod = load_solution("01_Arrays/0053_Maximum_Subarray.py")
        sol = mod.Solution()
        self.assertEqual(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_0054(self):
        mod = load_solution("01_Arrays/0054_Spiral_Matrix.py")
        sol = mod.Solution()
        self.assertEqual(sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_0055(self):
        mod = load_solution("01_Arrays/0055_Jump_Game.py")
        sol = mod.Solution()
        self.assertTrue(sol.canJump([2, 3, 1, 1, 4])); self.assertFalse(sol.canJump([3, 2, 1, 0, 4]))

    def test_0056(self):
        mod = load_solution("01_Arrays/0056_Merge_Intervals.py")
        sol = mod.Solution()
        self.assertEqual(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])

    def test_0057(self):
        mod = load_solution("01_Arrays/0057_Insert_Interval.py")
        sol = mod.Solution()
        self.assertEqual(sol.insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])

    def test_0059(self):
        mod = load_solution("01_Arrays/0059_Spiral_Matrix_II.py")
        sol = mod.Solution()
        self.assertEqual(sol.generateMatrix(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])

    def test_0066(self):
        mod = load_solution("01_Arrays/0066_Plus_One.py")
        sol = mod.Solution()
        self.assertEqual(sol.plusOne([9, 9]), [1, 0, 0])

    def test_0073(self):
        mod = load_solution("01_Arrays/0073_Set_Matrix_Zeroes.py")
        sol = mod.Solution()
        m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]; sol.setZeroes(m); self.assertEqual(m, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

    def test_0075(self):
        mod = load_solution("01_Arrays/0075_Sort_Colors.py")
        sol = mod.Solution()
        a = [2, 0, 2, 1, 1, 0]; sol.sortColors(a); self.assertEqual(a, [0, 0, 1, 1, 2, 2])



if __name__ == "__main__":
    unittest.main()
