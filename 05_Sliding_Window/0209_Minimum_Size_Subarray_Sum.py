# LeetCode: 209
# Title: Minimum Size Subarray Sum
# Difficulty: Medium
# Pattern: Sliding Window (Variable)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        best = float("inf")

        for right, value in enumerate(nums):
            window_sum += value
            while window_sum >= target:
                length = right - left + 1
                if length < best:
                    best = length
                window_sum -= nums[left]
                left += 1

        return 0 if best == float("inf") else int(best)
