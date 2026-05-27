# LeetCode: 169
# Title: Majority Element
# Difficulty: Easy
# Pattern: Boyer-Moore Voting Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate
