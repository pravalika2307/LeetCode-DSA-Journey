import unittest

from tests.helpers import ListNode, from_linked_list, load_solution, to_linked_list


class TestBinarySearch(unittest.TestCase):
    def test_0004(self):
        mod = load_solution("06_Binary_Search/0004_Median_Of_Two_Sorted_Arrays.py")
        sol = mod.Solution()
        self.assertEqual(sol.findMedianSortedArrays([1, 3], [2]), 2.0); self.assertEqual(sol.findMedianSortedArrays([1, 2], [3, 4]), 2.5)

    def test_0033(self):
        mod = load_solution("06_Binary_Search/0033_Search_In_Rotated_Sorted_Array.py")
        sol = mod.Solution()
        self.assertEqual(sol.search([4, 5, 6, 7, 0, 1, 2], 0), 4)

    def test_0034(self):
        mod = load_solution("06_Binary_Search/0034_Find_First_And_Last_Position_Of_Element_In_Sorted_Array.py")
        sol = mod.Solution()
        self.assertEqual(sol.searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])

    def test_0035(self):
        mod = load_solution("06_Binary_Search/0035_Search_Insert_Position.py")
        sol = mod.Solution()
        self.assertEqual(sol.searchInsert([1, 3, 5, 6], 5), 2); self.assertEqual(sol.searchInsert([1, 3, 5, 6], 2), 1)

    def test_0069(self):
        mod = load_solution("06_Binary_Search/0069_Sqrt_X.py")
        sol = mod.Solution()
        self.assertEqual(sol.mySqrt(8), 2); self.assertEqual(sol.mySqrt(0), 0)

    def test_0074(self):
        mod = load_solution("06_Binary_Search/0074_Search_A_2D_Matrix.py")
        sol = mod.Solution()
        self.assertTrue(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))

    def test_0081(self):
        mod = load_solution("06_Binary_Search/0081_Search_In_Rotated_Sorted_Array_II.py")
        sol = mod.Solution()
        self.assertTrue(sol.search([2, 5, 6, 0, 0, 1, 2], 0)); self.assertFalse(sol.search([2, 5, 6, 0, 0, 1, 2], 3))

    def test_0153(self):
        mod = load_solution("06_Binary_Search/0153_Find_Minimum_In_Rotated_Sorted_Array.py")
        sol = mod.Solution()
        self.assertEqual(sol.findMin([3, 4, 5, 1, 2]), 1)

    def test_0154(self):
        mod = load_solution("06_Binary_Search/0154_Find_Minimum_In_Rotated_Sorted_Array_II.py")
        sol = mod.Solution()
        self.assertEqual(sol.findMin([2, 2, 2, 0, 1]), 0)

    def test_0162(self):
        mod = load_solution("06_Binary_Search/0162_Find_Peak_Element.py")
        sol = mod.Solution()
        self.assertEqual(sol.findPeakElement([1, 2, 3, 1]), 2)

    def test_0275(self):
        mod = load_solution("06_Binary_Search/0275_H_Index_II.py")
        sol = mod.Solution()
        self.assertEqual(sol.hIndex([0, 1, 3, 5, 6]), 3)



if __name__ == "__main__":
    unittest.main()
