# LeetCode: 1695
# Title: Maximum Erasure Value
# Difficulty: Medium
# Pattern: Sliding Window (Variable) + Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = 0
        window_sum = 0
        best = 0

        for val in nums:
            while val in seen:
                seen.remove(nums[left])
                window_sum -= nums[left]
                left += 1
            seen.add(val)
            window_sum += val
            if window_sum > best:
                best = window_sum

        return best
