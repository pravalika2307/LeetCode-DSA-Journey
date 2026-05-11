# LeetCode: 53
# Title: Maximum Subarray
# Difficulty: Medium
# Pattern: Kadane's Algorithm / Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        best_sum = nums[0]

        for value in nums[1:]:
            current_sum = max(value, current_sum + value)
            if current_sum > best_sum:
                best_sum = current_sum

        return best_sum
