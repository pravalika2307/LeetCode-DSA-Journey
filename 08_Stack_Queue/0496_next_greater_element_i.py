# LeetCode: 496
# Title: Next Greater Element I
# Difficulty: Easy
# Pattern: Monotonic Stack
# Time Complexity: O(n + m)
# Space Complexity: O(m)

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        return [next_greater.get(x, -1) for x in nums1]
