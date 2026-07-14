# LeetCode: 447
# Title: Number of Boomerangs
# Difficulty: Medium
# Pattern: Hashing (Distance Frequency Map)
# Time Complexity: O(n^2)
# Space Complexity: O(n)

from collections import defaultdict
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0

        for x1, y1 in points:
            dist_counts = defaultdict(int)
            for x2, y2 in points:
                dx = x1 - x2
                dy = y1 - y2
                dist_counts[dx * dx + dy * dy] += 1

            for count in dist_counts.values():
                total += count * (count - 1)

        return total
