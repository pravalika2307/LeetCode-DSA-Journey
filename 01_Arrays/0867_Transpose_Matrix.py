# LeetCode: 867
# Title: Transpose Matrix
# Difficulty: Easy
# Pattern: Matrix Manipulation
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        result = [[0] * rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                result[c][r] = matrix[r][c]

        return result
