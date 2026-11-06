# LeetCode: 2187
# Title: Minimum Time to Complete Trips
# Difficulty: Medium
# Pattern: Binary Search on Answer
# Time Complexity: O(n log(min(time) * totalTrips))
# Space Complexity: O(1)

from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def can_complete(elapsed: int) -> bool:
            trips = 0
            for t in time:
                trips += elapsed // t
                if trips >= totalTrips:
                    return True
            return False

        left, right = 1, min(time) * totalTrips
        while left < right:
            mid = left + (right - left) // 2
            if can_complete(mid):
                right = mid
            else:
                left = mid + 1

        return left
