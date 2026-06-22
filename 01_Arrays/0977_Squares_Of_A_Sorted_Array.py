# LeetCode: 977
# Title: Squares of a Sorted Array
# Difficulty: Easy
# Pattern: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1

        for write in range(n - 1, -1, -1):
            if abs(nums[left]) >= abs(nums[right]):
                result[write] = nums[left] * nums[left]
                left += 1
            else:
                result[write] = nums[right] * nums[right]
                right -= 1

        return result
