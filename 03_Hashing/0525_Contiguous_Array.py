# LeetCode: 525
# Title: Contiguous Array
# Difficulty: Medium
# Pattern: Prefix Sum + Hash Map
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_seen = {0: -1}
        balance = 0
        best = 0

        for idx, value in enumerate(nums):
            balance += 1 if value == 1 else -1
            if balance in first_seen:
                length = idx - first_seen[balance]
                if length > best:
                    best = length
            else:
                first_seen[balance] = idx

        return best
