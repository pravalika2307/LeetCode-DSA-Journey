# LeetCode: 523
# Title: Continuous Subarray Sum
# Difficulty: Medium
# Pattern: Prefix Sum + Hash Map
# Time Complexity: O(n)
# Space Complexity: O(min(n, k))

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_idx = {0: -1}
        prefix_sum = 0

        for idx, num in enumerate(nums):
            prefix_sum += num
            rem = prefix_sum % k if k != 0 else prefix_sum
            if rem in remainder_idx:
                if idx - remainder_idx[rem] >= 2:
                    return True
            else:
                remainder_idx[rem] = idx

        return False
