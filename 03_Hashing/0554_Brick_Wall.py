# LeetCode: 554
# Title: Brick Wall
# Difficulty: Medium
# Pattern: Hashing (Edge Frequency Map)
# Time Complexity: O(total bricks)
# Space Complexity: O(width)

from collections import defaultdict
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_counts = defaultdict(int)
        max_edges = 0

        for row in wall:
            pos = 0
            for brick in row[:-1]:
                pos += brick
                edge_counts[pos] += 1
                if edge_counts[pos] > max_edges:
                    max_edges = edge_counts[pos]

        return len(wall) - max_edges
