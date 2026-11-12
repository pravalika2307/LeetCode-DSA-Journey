# LeetCode: 82
# Title: Remove Duplicates from Sorted List II
# Difficulty: Medium
# Pattern: Linked List Pointer Manipulation
# Time Complexity: O(n)
# Space Complexity: O(1)

from __future__ import annotations

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next is not None:
            curr = prev.next
            if curr.next is not None and curr.val == curr.next.val:
                dup_val = curr.val
                while curr is not None and curr.val == dup_val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = prev.next

        return dummy.next
