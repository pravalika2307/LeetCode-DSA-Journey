# LeetCode: 275
# Title: H-Index II
# Difficulty: Medium
# Pattern: Binary Search (Index Offset)
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            papers = n - mid
            if citations[mid] == papers:
                return papers
            if citations[mid] < papers:
                left = mid + 1
            else:
                right = mid - 1

        return n - left
