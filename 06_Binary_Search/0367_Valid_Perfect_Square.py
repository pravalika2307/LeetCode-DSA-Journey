# LeetCode: 367
# Title: Valid Perfect Square
# Difficulty: Easy
# Pattern: Binary Search on Answer
# Time Complexity: O(log num)
# Space Complexity: O(1)


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        left, right = 2, num // 2
        while left <= right:
            mid = left + (right - left) // 2
            sq = mid * mid
            if sq == num:
                return True
            if sq < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
