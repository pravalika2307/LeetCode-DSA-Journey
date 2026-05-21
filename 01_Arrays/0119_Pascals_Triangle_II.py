# LeetCode: 119
# Title: Pascal's Triangle II
# Difficulty: Easy
# Pattern: 1D Rolling Dynamic Programming
# Time Complexity: O(rowIndex^2)
# Space Complexity: O(rowIndex)

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)

        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]

        return row
