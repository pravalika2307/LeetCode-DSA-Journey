# LeetCode: 2302
# Title: Count Subarrays With Score Less Than K
# Difficulty: Hard
# Pattern: Sliding Window (Variable)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        left = 0
        window_sum = 0
        total = 0

        for right, value in enumerate(nums):
            window_sum += value
            while left <= right and window_sum * (right - left + 1) >= k:
                window_sum -= nums[left]
                left += 1
            total += right - left + 1

        return total
