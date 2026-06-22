# LeetCode: 1013
# Title: Partition Array Into Three Parts With Equal Sum
# Difficulty: Easy
# Pattern: Prefix Sum / Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False

        target = total // 3
        running = 0
        parts = 0

        for idx, value in enumerate(arr):
            running += value
            if running == target:
                parts += 1
                running = 0
                if parts == 2 and idx < len(arr) - 1:
                    return True

        return False
