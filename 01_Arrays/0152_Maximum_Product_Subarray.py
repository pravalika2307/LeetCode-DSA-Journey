# LeetCode: 152
# Title: Maximum Product Subarray
# Difficulty: Medium
# Pattern: Dynamic Programming / Running Min-Max
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        best = nums[0]

        for val in nums[1:]:
            candidates = (val, cur_max * val, cur_min * val)
            cur_max = max(candidates)
            cur_min = min(candidates)
            if cur_max > best:
                best = cur_max

        return best
