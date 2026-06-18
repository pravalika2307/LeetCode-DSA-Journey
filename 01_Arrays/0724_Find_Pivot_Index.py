# LeetCode: 724
# Title: Find Pivot Index
# Difficulty: Easy
# Pattern: Prefix Sum
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for idx, value in enumerate(nums):
            if left_sum == total_sum - left_sum - value:
                return idx
            left_sum += value

        return -1
