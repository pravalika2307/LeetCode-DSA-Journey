import unittest

from tests.helpers import ListNode, from_linked_list, load_solution, to_linked_list


class TestLinkedList(unittest.TestCase):
    def test_0002(self):
        mod = load_solution("07_Linked_List/0002_Add_Two_Numbers.py")
        sol = mod.Solution()
        self.assertEqual(from_linked_list(sol.addTwoNumbers(to_linked_list([2, 4, 3]), to_linked_list([5, 6, 4]))), [7, 0, 8])



if __name__ == "__main__":
    unittest.main()
