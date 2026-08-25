# LeetCode: 633
# Title: Sum of Square Numbers
# Difficulty: Medium
# Pattern: Two Pointers (Search Space)
# Time Complexity: O(sqrt(c))
# Space Complexity: O(1)

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = math.isqrt(c)

        while left <= right:
            total = left * left + right * right
            if total == c:
                return True
            if total < c:
                left += 1
            else:
                right -= 1

        return False
