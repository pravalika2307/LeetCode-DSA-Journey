# LeetCode: 162
# Title: Find Peak Element
# Difficulty: Medium
# Pattern: Binary Search (Peak Finding)
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left
