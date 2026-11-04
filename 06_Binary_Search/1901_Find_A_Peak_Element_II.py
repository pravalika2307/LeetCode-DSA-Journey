# LeetCode: 1901
# Title: Find a Peak Element II
# Difficulty: Medium
# Pattern: Binary Search (2D Matrix Column Search)
# Time Complexity: O(m log n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        left, right = 0, cols - 1

        while left <= right:
            mid_col = left + (right - left) // 2
            max_row = 0
            for r in range(1, rows):
                if mat[r][mid_col] > mat[max_row][mid_col]:
                    max_row = r

            left_val = mat[max_row][mid_col - 1] if mid_col > 0 else -1
            right_val = mat[max_row][mid_col + 1] if mid_col + 1 < cols else -1

            if mat[max_row][mid_col] > left_val and mat[max_row][mid_col] > right_val:
                return [max_row, mid_col]
            if left_val > mat[max_row][mid_col]:
                right = mid_col - 1
            else:
                left = mid_col + 1

        return [-1, -1]
