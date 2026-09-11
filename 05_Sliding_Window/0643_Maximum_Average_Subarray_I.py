# LeetCode: 643
# Title: Maximum Average Subarray I
# Difficulty: Easy
# Pattern: Sliding Window (Fixed)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for right in range(k, len(nums)):
            window_sum += nums[right] - nums[right - k]
            if window_sum > max_sum:
                max_sum = window_sum

        return max_sum / k
