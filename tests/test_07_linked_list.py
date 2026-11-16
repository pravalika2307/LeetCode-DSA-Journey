import unittest

from tests.helpers import ListNode, from_linked_list, load_solution, to_linked_list


class TestLinkedList(unittest.TestCase):
    def test_0002(self):
        mod = load_solution("07_Linked_List/0002_Add_Two_Numbers.py")
        sol = mod.Solution()
        self.assertEqual(from_linked_list(sol.addTwoNumbers(to_linked_list([2, 4, 3]), to_linked_list([5, 6, 4]))), [7, 0, 8])

    def test_0019(self):
        mod = load_solution("07_Linked_List/0019_Remove_Nth_Node_From_End_Of_List.py")
        sol = mod.Solution()
        self.assertEqual(from_linked_list(sol.removeNthFromEnd(to_linked_list([1, 2, 3, 4, 5]), 2)), [1, 2, 3, 5])

    def test_0021(self):
        mod = load_solution("07_Linked_List/0021_Merge_Two_Sorted_Lists.py")
        sol = mod.Solution()
        self.assertEqual(from_linked_list(sol.mergeTwoLists(to_linked_list([1, 2, 4]), to_linked_list([1, 3, 4]))), [1, 1, 2, 3, 4, 4])

    def test_0023(self):
        mod = load_solution("07_Linked_List/0023_Merge_K_Sorted_Lists.py")
        sol = mod.Solution()
        self.assertEqual(from_linked_list(sol.mergeKLists([to_linked_list([1, 4, 5]), to_linked_list([1, 3, 4]), to_linked_list([2, 6])])), [1, 1, 2, 3, 4, 4, 5, 6])

    def test_0024(self):
        mod = load_solution("07_Linked_List/0024_Swap_Nodes_In_Pairs.py")
        sol = mod.Solution()
        self.assertEqual(from_linked_list(sol.swapPairs(to_linked_list([1, 2, 3, 4]))), [2, 1, 4, 3])

    def test_0025(self):
        mod = load_solution("07_Linked_List/0025_Reverse_Nodes_In_K_Group.py")
        sol = mod.Solution()
        self.assertEqual(from_linked_list(sol.reverseKGroup(to_linked_list([1, 2, 3, 4, 5]), 2)), [2, 1, 4, 3, 5])

    def test_0061(self):
        mod = load_solution("07_Linked_List/0061_Rotate_List.py")
        sol = mod.Solution()
        self.assertEqual(from_linked_list(sol.rotateRight(to_linked_list([1, 2, 3, 4, 5]), 2)), [4, 5, 1, 2, 3])

    def test_0082(self):
        mod = load_solution("07_Linked_List/0082_Remove_Duplicates_From_Sorted_List_II.py")
        sol = mod.Solution()
        self.assertEqual(from_linked_list(sol.deleteDuplicates(to_linked_list([1, 2, 3, 3, 4, 4, 5]))), [1, 2, 5])

    def test_0083(self):
        mod = load_solution("07_Linked_List/0083_Remove_Duplicates_From_Sorted_List.py")
        sol = mod.Solution()
        self.assertEqual(from_linked_list(sol.deleteDuplicates(to_linked_list([1, 1, 2, 3, 3]))), [1, 2, 3])

    def test_0086(self):
        mod = load_solution("07_Linked_List/0086_Partition_List.py")
        sol = mod.Solution()
        self.assertEqual(from_linked_list(sol.partition(to_linked_list([1, 4, 3, 2, 5, 2]), 3)), [1, 2, 2, 4, 3, 5])



if __name__ == "__main__":
    unittest.main()
