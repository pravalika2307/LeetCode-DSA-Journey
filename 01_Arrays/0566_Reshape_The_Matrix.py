# LeetCode: 566
# Title: Reshape the Matrix
# Difficulty: Easy
# Pattern: Matrix Index Mapping
# Time Complexity: O(m * n)
# Space Complexity: O(r * c)

from typing import List


class Solution:
    def matrixReshape(
        self, mat: List[List[int]], r: int, c: int
    ) -> List[List[int]]:
        if not mat or not mat[0]:
            return mat

        rows, cols = len(mat), len(mat[0])
        if rows * cols != r * c:
            return mat

        reshaped = [[0] * c for _ in range(r)]
        for idx in range(rows * cols):
            reshaped[idx // c][idx % c] = mat[idx // cols][idx % cols]

        return reshaped
