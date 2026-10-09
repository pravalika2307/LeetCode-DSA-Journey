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



if __name__ == "__main__":
    unittest.main()
