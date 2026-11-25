# LeetCode: 1290
# Title: Convert Binary Number in a Linked List to Integer
# Difficulty: Easy
# Pattern: Linked List Traversal / Bit Manipulation
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
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        value = 0
        curr = head
        while curr is not None:
            value = (value << 1) | curr.val
            curr = curr.next
        return value
