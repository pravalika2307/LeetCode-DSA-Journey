# LeetCode: 1658
# Title: Minimum Operations to Reduce X to Zero
# Difficulty: Medium
# Pattern: Sliding Window (Complement Target Sum)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        left = 0
        window_sum = 0
        best_len = -1

        for right, val in enumerate(nums):
            window_sum += val
            while window_sum > target and left <= right:
                window_sum -= nums[left]
                left += 1
            if window_sum == target:
                best_len = max(best_len, right - left + 1)

        return -1 if best_len == -1 else len(nums) - best_len
