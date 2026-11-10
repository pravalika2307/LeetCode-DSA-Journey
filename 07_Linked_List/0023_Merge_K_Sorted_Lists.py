# LeetCode: 23
# Title: Merge k Sorted Lists
# Difficulty: Hard
# Pattern: Linked List Divide and Conquer
# Time Complexity: O(N log k)
# Space Complexity: O(log k)

from __future__ import annotations

from typing import List, Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        if not lists:
            return None

        def merge_two(
            l1: Optional[ListNode], l2: Optional[ListNode]
        ) -> Optional[ListNode]:
            dummy = ListNode(0)
            tail = dummy
            while l1 is not None and l2 is not None:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 if l1 is not None else l2
            return dummy.next

        interval = 1
        n = len(lists)
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = merge_two(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]
