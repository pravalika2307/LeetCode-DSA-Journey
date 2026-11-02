# LeetCode: 1608
# Title: Special Array With X Elements Greater Than or Equal X
# Difficulty: Easy
# Pattern: Binary Search + Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(1) auxiliary

from bisect import bisect_left
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        for x in range(1, n + 1):
            idx = bisect_left(nums, x)
            if n - idx == x:
                return x

        return -1
