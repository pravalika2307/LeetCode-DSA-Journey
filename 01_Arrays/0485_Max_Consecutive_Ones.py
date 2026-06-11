# LeetCode: 485
# Title: Max Consecutive Ones
# Difficulty: Easy
# Pattern: Array Linear Scan
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        current = 0

        for num in nums:
            if num == 1:
                current += 1
                if current > best:
                    best = current
            else:
                current = 0

        return best
