# LeetCode: 445
# Title: Add Two Numbers II
# Difficulty: Medium
# Pattern: Linked List + Stack Math
# Time Complexity: O(m + n)
# Space Complexity: O(m + n)

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
        stack1 = []
        stack2 = []

        while l1 is not None:
            stack1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head: Optional[ListNode] = None

        while stack1 or stack2 or carry:
            v1 = stack1.pop() if stack1 else 0
            v2 = stack2.pop() if stack2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            head = ListNode(total % 10, head)

        return head
