# LeetCode: 189
# Title: Rotate Array
# Difficulty: Medium
# Pattern: Array Reversal
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n <= 1:
            return

        steps = k % n
        if steps == 0:
            return

        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, steps - 1)
        reverse(steps, n - 1)
