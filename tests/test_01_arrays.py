import unittest

from tests.helpers import ListNode, from_linked_list, load_solution, to_linked_list


class TestArrays(unittest.TestCase):
    def test_0001(self):
        mod = load_solution("01_Arrays/0001_Two_Sum.py")
        sol = mod.Solution()
        self.assertEqual(sol.twoSum([2, 7, 11, 15], 9), [0, 1])



if __name__ == "__main__":
    unittest.main()
