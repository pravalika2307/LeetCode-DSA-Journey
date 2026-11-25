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

    def test_0092(self):
        mod = load_solution("07_Linked_List/0092_Reverse_Linked_List_II.py")
        sol = mod.Solution()
        self.assertEqual(from_linked_list(sol.reverseBetween(to_linked_list([1, 2, 3, 4, 5]), 2, 4)), [1, 4, 3, 2, 5])

    def test_0141(self):
        mod = load_solution("07_Linked_List/0141_Linked_List_Cycle.py")
        sol = mod.Solution()
        n1, n2 = ListNode(3), ListNode(2); n1.next, n2.next = n2, n1; self.assertTrue(sol.hasCycle(n1)); self.assertFalse(sol.hasCycle(to_linked_list([1, 2])))

    def test_0142(self):
        mod = load_solution("07_Linked_List/0142_Linked_List_Cycle_II.py")
        sol = mod.Solution()
        n1, n2, n3 = ListNode(3), ListNode(2), ListNode(0); n1.next, n2.next, n3.next = n2, n3, n2; self.assertIs(sol.detectCycle(n1), n2)

    def test_0143(self):
        mod = load_solution("07_Linked_List/0143_Reorder_List.py")
        sol = mod.Solution()
        head = to_linked_list([1, 2, 3, 4, 5]); sol.reorderList(head); self.assertEqual(from_linked_list(head), [1, 5, 2, 4, 3])

    def test_0148(self):
        mod = load_solution("07_Linked_List/0148_Sort_List.py")
        sol = mod.Solution()
        self.assertEqual(from_linked_list(sol.sortList(to_linked_list([4, 2, 1, 3]))), [1, 2, 3, 4])

    def test_0160(self):
        mod = load_solution("07_Linked_List/0160_Intersection_Of_Two_Linked_Lists.py")
        sol = mod.Solution()
        shared = ListNode(8, ListNode(4)); a = ListNode(4, ListNode(1, shared)); b = ListNode(5, shared); self.assertIs(sol.getIntersectionNode(a, b), shared)

    def test_0203(self):
        mod = load_solution("07_Linked_List/0203_Remove_Linked_List_Elements.py")
        sol = mod.Solution()
        self.assertEqual(from_linked_list(sol.removeElements(to_linked_list([1, 2, 6, 3, 4, 5, 6]), 6)), [1, 2, 3, 4, 5])

    def test_0206(self):
        mod = load_solution("07_Linked_List/0206_Reverse_Linked_List.py")
        sol = mod.Solution()
        self.assertEqual(from_linked_list(sol.reverseList(to_linked_list([1, 2, 3, 4, 5]))), [5, 4, 3, 2, 1])

    def test_0234(self):
        mod = load_solution("07_Linked_List/0234_Palindrome_Linked_List.py")
        sol = mod.Solution()
        self.assertTrue(sol.isPalindrome(to_linked_list([1, 2, 2, 1]))); self.assertFalse(sol.isPalindrome(to_linked_list([1, 2])))

    def test_0237(self):
        mod = load_solution("07_Linked_List/0237_Delete_Node_In_A_Linked_List.py")
        sol = mod.Solution()
        head = to_linked_list([4, 5, 1, 9]); sol.deleteNode(head.next); self.assertEqual(from_linked_list(head), [4, 1, 9])

    def test_0328(self):
        mod = load_solution("07_Linked_List/0328_Odd_Even_Linked_List.py")
        sol = mod.Solution()
        self.assertEqual(from_linked_list(sol.oddEvenList(to_linked_list([1, 2, 3, 4, 5]))), [1, 3, 5, 2, 4])

    def test_0445(self):
        mod = load_solution("07_Linked_List/0445_Add_Two_Numbers_II.py")
        sol = mod.Solution()
        self.assertEqual(from_linked_list(sol.addTwoNumbers(to_linked_list([7, 2, 4, 3]), to_linked_list([5, 6, 4]))), [7, 8, 0, 7])

    def test_0876(self):
        mod = load_solution("07_Linked_List/0876_Middle_Of_The_Linked_List.py")
        sol = mod.Solution()
        self.assertEqual(from_linked_list(sol.middleNode(to_linked_list([1, 2, 3, 4, 5]))), [3, 4, 5])

    def test_1290(self):
        mod = load_solution("07_Linked_List/1290_Convert_Binary_Number_In_A_Linked_List_To_Integer.py")
        sol = mod.Solution()
        self.assertEqual(sol.getDecimalValue(to_linked_list([1, 0, 1])), 5)


if __name__ == "__main__":
    unittest.main()
