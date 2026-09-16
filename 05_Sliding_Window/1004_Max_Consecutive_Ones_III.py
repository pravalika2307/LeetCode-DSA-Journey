# LeetCode: 1004
# Title: Max Consecutive Ones III
# Difficulty: Medium
# Pattern: Sliding Window (Variable)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        best = 0

        for right, value in enumerate(nums):
            if value == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            length = right - left + 1
            if length > best:
                best = length

        return best
