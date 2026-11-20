# LeetCode: 234
# Title: Palindrome Linked List
# Difficulty: Easy
# Pattern: Linked List Fast & Slow + Reversal
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        left = head
        right = prev
        while right is not None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
