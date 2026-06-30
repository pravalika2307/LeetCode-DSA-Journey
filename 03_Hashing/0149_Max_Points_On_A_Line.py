# LeetCode: 149
# Title: Max Points on a Line
# Difficulty: Hard
# Pattern: Hashing (Slope Frequency Map)
# Time Complexity: O(n^2)
# Space Complexity: O(n)

from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        best = 1
        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]
            local_max = 0

            for j in range(i + 1, n):
                dx = points[j][0] - x1
                dy = points[j][1] - y1
                g = gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g

                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = 1

                slopes[(dx, dy)] += 1
                if slopes[(dx, dy)] > local_max:
                    local_max = slopes[(dx, dy)]

            if local_max + 1 > best:
                best = local_max + 1

        return best
