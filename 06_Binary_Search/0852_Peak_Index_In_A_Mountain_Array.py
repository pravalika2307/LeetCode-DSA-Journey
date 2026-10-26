# LeetCode: 852
# Title: Peak Index in a Mountain Array
# Difficulty: Medium
# Pattern: Binary Search (Mountain Array)
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
