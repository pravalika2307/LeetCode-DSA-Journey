# LeetCode: 61
# Title: Rotate List
# Difficulty: Medium
# Pattern: Linked List Cycle / Length Modulo
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head

        length = 1
        tail = head
        while tail.next is not None:
            tail = tail.next
            length += 1

        steps = k % length
        if steps == 0:
            return head

        tail.next = head
        new_tail = head
        for _ in range(length - steps - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head
