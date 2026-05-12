# LeetCode: 55
# Title: Jump Game
# Difficulty: Medium
# Pattern: Greedy Reachability
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        last_idx = len(nums) - 1

        for idx, jump in enumerate(nums):
            if idx > farthest:
                return False
            if idx + jump > farthest:
                farthest = idx + jump
            if farthest >= last_idx:
                return True

        return True
