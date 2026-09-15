# LeetCode: 930
# Title: Binary Subarrays With Sum
# Difficulty: Medium
# Pattern: Sliding Window (At Most Goal Difference)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def count_at_most(target: int) -> int:
            if target < 0:
                return 0
            left = 0
            window_sum = 0
            total = 0
            for right, value in enumerate(nums):
                window_sum += value
                while window_sum > target:
                    window_sum -= nums[left]
                    left += 1
                total += right - left + 1
            return total

        return count_at_most(goal) - count_at_most(goal - 1)
