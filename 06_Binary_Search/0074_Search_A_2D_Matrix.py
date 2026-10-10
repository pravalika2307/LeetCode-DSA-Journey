# LeetCode: 74
# Title: Search a 2D Matrix
# Difficulty: Medium
# Pattern: Binary Search (2D Matrix)
# Time Complexity: O(log(m * n))
# Space Complexity: O(1)

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            value = matrix[mid // cols][mid % cols]
            if value == target:
                return True
            if value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
