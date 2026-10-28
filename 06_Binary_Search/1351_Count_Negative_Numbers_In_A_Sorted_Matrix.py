# LeetCode: 1351
# Title: Count Negative Numbers in a Sorted Matrix
# Difficulty: Easy
# Pattern: Matrix Staircase / Binary Search
# Time Complexity: O(m + n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        r, c = rows - 1, 0
        negatives = 0

        while r >= 0 and c < cols:
            if grid[r][c] < 0:
                negatives += cols - c
                r -= 1
            else:
                c += 1

        return negatives
