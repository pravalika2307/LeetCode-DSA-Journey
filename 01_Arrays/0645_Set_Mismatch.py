# LeetCode: 645
# Title: Set Mismatch
# Difficulty: Easy
# Pattern: In-Place Cyclic Marking
# Time Complexity: O(n)
# Space Complexity: O(1) auxiliary

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = -1
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                duplicate = abs(num)
            else:
                nums[idx] = -nums[idx]

        missing = -1
        for idx, value in enumerate(nums):
            if value > 0:
                missing = idx + 1
                break

        return [duplicate, missing]
