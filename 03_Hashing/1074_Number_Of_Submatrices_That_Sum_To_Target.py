# LeetCode: 1074
# Title: Number of Submatrices That Sum to Target
# Difficulty: Hard
# Pattern: Prefix Sum + Hash Map (2D Reduction)
# Time Complexity: O(rows^2 * cols)
# Space Complexity: O(cols)

from collections import defaultdict
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        total = 0

        for top in range(rows):
            col_sums = [0] * cols
            for bottom in range(top, rows):
                for c in range(cols):
                    col_sums[c] += matrix[bottom][c]

                prefix_counts = defaultdict(int)
                prefix_counts[0] = 1
                running = 0
                for val in col_sums:
                    running += val
                    total += prefix_counts[running - target]
                    prefix_counts[running] += 1

        return total
