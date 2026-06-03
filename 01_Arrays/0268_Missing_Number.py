# LeetCode: 268
# Title: Missing Number
# Difficulty: Easy
# Pattern: Bit Manipulation (XOR)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for idx, num in enumerate(nums):
            missing ^= idx ^ num
        return missing
