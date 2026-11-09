# LeetCode: 19
# Title: Remove Nth Node From End of List
# Difficulty: Medium
# Pattern: Linked List Two Pointers (Fast & Slow)
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n):
            if fast.next is None:
                return head
            fast = fast.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        if slow.next is not None:
            slow.next = slow.next.next

        return dummy.next
