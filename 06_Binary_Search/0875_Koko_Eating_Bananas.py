# LeetCode: 875
# Title: Koko Eating Bananas
# Difficulty: Medium
# Pattern: Binary Search on Answer
# Time Complexity: O(n log(max(piles)))
# Space Complexity: O(1)

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(speed: int) -> bool:
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed
            return hours <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left
