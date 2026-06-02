# LeetCode: 240
# Title: Search a 2D Matrix II
# Difficulty: Medium
# Pattern: Matrix Staircase Search
# Time Complexity: O(m + n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols - 1

        while r < rows and c >= 0:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                c -= 1
            else:
                r += 1

        return False
