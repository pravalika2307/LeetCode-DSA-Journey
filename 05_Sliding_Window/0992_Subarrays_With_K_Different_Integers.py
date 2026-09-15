# LeetCode: 992
# Title: Subarrays with K Different Integers
# Difficulty: Hard
# Pattern: Sliding Window (At Most K Difference)
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def count_at_most(distinct_limit: int) -> int:
            if distinct_limit <= 0:
                return 0
            counts = defaultdict(int)
            left = 0
            total = 0
            for right, value in enumerate(nums):
                counts[value] += 1
                while len(counts) > distinct_limit:
                    left_val = nums[left]
                    counts[left_val] -= 1
                    if counts[left_val] == 0:
                        del counts[left_val]
                    left += 1
                total += right - left + 1
            return total

        return count_at_most(k) - count_at_most(k - 1)
