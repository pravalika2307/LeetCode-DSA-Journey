# LeetCode: 160
# Title: Intersection of Two Linked Lists
# Difficulty: Easy
# Pattern: Linked List Two Pointers
# Time Complexity: O(m + n)
# Space Complexity: O(1)

from __future__ import annotations

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        p_a: Optional[ListNode] = headA
        p_b: Optional[ListNode] = headB

        while p_a is not p_b:
            p_a = p_a.next if p_a is not None else headB
            p_b = p_b.next if p_b is not None else headA

        return p_a
