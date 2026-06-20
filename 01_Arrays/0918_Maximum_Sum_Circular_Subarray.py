# LeetCode: 918
# Title: Maximum Sum Circular Subarray
# Difficulty: Medium
# Pattern: Kadane's Algorithm (Circular Variant)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        cur_max = 0
        max_sum = nums[0]
        cur_min = 0
        min_sum = nums[0]

        for num in nums:
            total += num
            cur_max = max(num, cur_max + num)
            max_sum = max(max_sum, cur_max)
            cur_min = min(num, cur_min + num)
            min_sum = min(min_sum, cur_min)

        if max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum)
