# LeetCode: 86
# Title: Partition List
# Difficulty: Medium
# Pattern: Linked List Two-List Partitioning
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_dummy = ListNode(0)
        after_dummy = ListNode(0)
        before = before_dummy
        after = after_dummy

        curr = head
        while curr is not None:
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next
            curr = curr.next

        after.next = None
        before.next = after_dummy.next
        return before_dummy.next
