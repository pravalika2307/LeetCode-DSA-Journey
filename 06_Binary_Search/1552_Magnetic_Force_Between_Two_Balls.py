# LeetCode: 1552
# Title: Magnetic Force Between Two Balls
# Difficulty: Medium
# Pattern: Binary Search on Answer + Sorting
# Time Complexity: O(n log n + n log(max(position) - min(position)))
# Space Complexity: O(1) auxiliary

from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def can_place(min_dist: int) -> bool:
            balls = 1
            last_pos = position[0]
            for pos in position[1:]:
                if pos - last_pos >= min_dist:
                    balls += 1
                    last_pos = pos
                    if balls == m:
                        return True
            return False

        left, right = 1, position[-1] - position[0]
        ans = 1

        while left <= right:
            mid = left + (right - left) // 2
            if can_place(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
