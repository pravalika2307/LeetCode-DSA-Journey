# LeetCode: 278
# Title: First Bad Version
# Difficulty: Easy
# Pattern: Binary Search (Lower Bound)
# Time Complexity: O(log n)
# Space Complexity: O(1)

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):  # noqa: F821
                right = mid
            else:
                left = mid + 1

        return left
