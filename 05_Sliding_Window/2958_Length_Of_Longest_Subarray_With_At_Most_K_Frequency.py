# LeetCode: 2958
# Title: Length of Longest Subarray With at Most K Frequency
# Difficulty: Medium
# Pattern: Sliding Window (Variable) + Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        left = 0
        best = 0

        for right, value in enumerate(nums):
            counts[value] += 1
            while counts[value] > k:
                counts[nums[left]] -= 1
                left += 1

            length = right - left + 1
            if length > best:
                best = length

        return best
