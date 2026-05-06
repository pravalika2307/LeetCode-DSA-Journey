# LeetCode: 1
# Title: Two Sum
# Difficulty: Easy
# Pattern: Hashing (Hash Map)
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement], index]
            seen[value] = index
        return []
