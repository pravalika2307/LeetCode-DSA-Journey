# LeetCode: 1493
# Title: Longest Subarray of 1's After Deleting One Element
# Difficulty: Medium
# Pattern: Sliding Window (Variable)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        best = 0

        for right, value in enumerate(nums):
            if value == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            length = right - left
            if length > best:
                best = length

        return best
