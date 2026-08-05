# LeetCode: 11
# Title: Container With Most Water
# Difficulty: Medium
# Pattern: Two Pointers (Opposite Ends)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0

        while left < right:
            width = right - left
            area = width * min(height[left], height[right])
            if area > best:
                best = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return best
