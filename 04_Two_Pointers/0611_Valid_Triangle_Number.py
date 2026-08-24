# LeetCode: 611
# Title: Valid Triangle Number
# Difficulty: Medium
# Pattern: Two Pointers + Sorting
# Time Complexity: O(n^2)
# Space Complexity: O(1) auxiliary

from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        for longest in range(len(nums) - 1, 1, -1):
            left, right = 0, longest - 1
            while left < right:
                if nums[left] + nums[right] > nums[longest]:
                    count += right - left
                    right -= 1
                else:
                    left += 1

        return count
