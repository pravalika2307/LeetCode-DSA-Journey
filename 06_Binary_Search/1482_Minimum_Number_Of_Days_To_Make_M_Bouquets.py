# LeetCode: 1482
# Title: Minimum Number of Days to Make m Bouquets
# Difficulty: Medium
# Pattern: Binary Search on Answer
# Time Complexity: O(n log(max(bloomDay)))
# Space Complexity: O(1)

from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def can_make(day: int) -> bool:
            bouquets = 0
            consecutive = 0
            for bloom in bloomDay:
                if bloom <= day:
                    consecutive += 1
                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0
                else:
                    consecutive = 0
            return bouquets >= m

        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if can_make(mid):
                right = mid
            else:
                left = mid + 1

        return left
