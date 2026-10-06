import unittest

from tests.helpers import ListNode, from_linked_list, load_solution, to_linked_list


class TestBinarySearch(unittest.TestCase):
    def test_0004(self):
        mod = load_solution("06_Binary_Search/0004_Median_Of_Two_Sorted_Arrays.py")
        sol = mod.Solution()
        self.assertEqual(sol.findMedianSortedArrays([1, 3], [2]), 2.0); self.assertEqual(sol.findMedianSortedArrays([1, 2], [3, 4]), 2.5)



if __name__ == "__main__":
    unittest.main()
