# LeetCode: 118
# Title: Pascal's Triangle
# Difficulty: Easy
# Pattern: Dynamic Programming / Array Construction
# Time Complexity: O(numRows^2)
# Space Complexity: O(1) auxiliary

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle: List[List[int]] = []

        for row_idx in range(numRows):
            row = [1] * (row_idx + 1)
            for col in range(1, row_idx):
                row[col] = triangle[row_idx - 1][col - 1] + triangle[row_idx - 1][col]
            triangle.append(row)

        return triangle
