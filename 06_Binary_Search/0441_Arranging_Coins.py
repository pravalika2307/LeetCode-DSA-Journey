# LeetCode: 441
# Title: Arranging Coins
# Difficulty: Easy
# Pattern: Binary Search on Answer
# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n

        while left <= right:
            mid = left + (right - left) // 2
            needed = mid * (mid + 1) // 2
            if needed == n:
                return mid
            if needed < n:
                left = mid + 1
            else:
                right = mid - 1

        return right
