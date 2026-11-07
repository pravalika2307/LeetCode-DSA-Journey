# LeetCode: 2
# Title: Add Two Numbers
# Difficulty: Medium
# Pattern: Linked List Traversal / Carry Math
# Time Complexity: O(max(m, n))
# Space Complexity: O(max(m, n))

from __future__ import annotations

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry:
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0

            total = v1 + v2 + carry
            carry = total // 10
            tail.next = ListNode(total % 10)
            tail = tail.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy.next
