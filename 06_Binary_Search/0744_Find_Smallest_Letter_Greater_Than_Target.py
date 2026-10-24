# LeetCode: 744
# Title: Find Smallest Letter Greater Than Target
# Difficulty: Easy
# Pattern: Binary Search (Upper Bound)
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return letters[left % len(letters)]
