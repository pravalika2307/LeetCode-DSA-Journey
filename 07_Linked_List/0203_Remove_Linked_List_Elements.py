# LeetCode: 203
# Title: Remove Linked List Elements
# Difficulty: Easy
# Pattern: Linked List Traversal (Dummy Head)
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
    def removeElements(
        self, head: Optional[ListNode], val: int
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy

        while curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next
