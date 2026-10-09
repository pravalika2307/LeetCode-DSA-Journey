# LeetCode: 69
# Title: Sqrt(x)
# Difficulty: Easy
# Pattern: Binary Search on Answer
# Time Complexity: O(log x)
# Space Complexity: O(1)


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2
        ans = 1

        while left <= right:
            mid = left + (right - left) // 2
            sq = mid * mid
            if sq == x:
                return mid
            if sq < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
