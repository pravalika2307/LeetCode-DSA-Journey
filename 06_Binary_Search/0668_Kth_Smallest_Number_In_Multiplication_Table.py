# LeetCode: 668
# Title: Kth Smallest Number in Multiplication Table
# Difficulty: Hard
# Pattern: Binary Search on Answer
# Time Complexity: O(m log(m * n))
# Space Complexity: O(1)


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count_less_equal(target: int) -> int:
            total = 0
            for row in range(1, m + 1):
                total += min(n, target // row)
            return total

        left, right = 1, m * n
        while left < right:
            mid = left + (right - left) // 2
            if count_less_equal(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
