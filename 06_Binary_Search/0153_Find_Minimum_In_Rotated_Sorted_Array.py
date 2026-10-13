# LeetCode: 153
# Title: Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# Pattern: Binary Search (Rotated Array)
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
