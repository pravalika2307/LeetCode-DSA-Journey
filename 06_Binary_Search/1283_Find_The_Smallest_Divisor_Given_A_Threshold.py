# LeetCode: 1283
# Title: Find the Smallest Divisor Given a Threshold
# Difficulty: Medium
# Pattern: Binary Search on Answer
# Time Complexity: O(n log(max(nums)))
# Space Complexity: O(1)

from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def within_threshold(divisor: int) -> bool:
            total = 0
            for num in nums:
                total += (num + divisor - 1) // divisor
            return total <= threshold

        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if within_threshold(mid):
                right = mid
            else:
                left = mid + 1

        return left
