# LeetCode: 498
# Title: Diagonal Traverse
# Difficulty: Medium
# Pattern: Matrix Diagonal Simulation
# Time Complexity: O(m * n)
# Space Complexity: O(1) auxiliary

from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        rows, cols = len(mat), len(mat[0])
        result: List[int] = []
        r, c = 0, 0
        going_up = True

        for _ in range(rows * cols):
            result.append(mat[r][c])
            if going_up:
                if c == cols - 1:
                    r += 1
                    going_up = False
                elif r == 0:
                    c += 1
                    going_up = False
                else:
                    r -= 1
                    c += 1
            else:
                if r == rows - 1:
                    c += 1
                    going_up = True
                elif c == 0:
                    r += 1
                    going_up = True
                else:
                    r += 1
                    c -= 1

        return result
