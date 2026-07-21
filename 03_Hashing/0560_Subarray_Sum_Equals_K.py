# LeetCode: 560
# Title: Subarray Sum Equals K
# Difficulty: Medium
# Pattern: Prefix Sum + Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        running_sum = 0
        subarrays = 0

        for num in nums:
            running_sum += num
            subarrays += prefix_counts[running_sum - k]
            prefix_counts[running_sum] += 1

        return subarrays
