# LeetCode: 330
# Title: Patching Array
# Difficulty: Hard
# Pattern: Greedy (Reachable Range)
# Time Complexity: O(m + log n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        patches = 0
        idx = 0

        while miss <= n:
            if idx < len(nums) and nums[idx] <= miss:
                miss += nums[idx]
                idx += 1
            else:
                miss += miss
                patches += 1

        return patches
