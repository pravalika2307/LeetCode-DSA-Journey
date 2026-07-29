# LeetCode: 974
# Title: Subarray Sums Divisible by K
# Difficulty: Medium
# Pattern: Prefix Sum + Hash Map
# Time Complexity: O(n)
# Space Complexity: O(k)

from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_counts = defaultdict(int)
        rem_counts[0] = 1
        prefix_sum = 0
        subarrays = 0

        for num in nums:
            prefix_sum += num
            rem = prefix_sum % k
            subarrays += rem_counts[rem]
            rem_counts[rem] += 1

        return subarrays
