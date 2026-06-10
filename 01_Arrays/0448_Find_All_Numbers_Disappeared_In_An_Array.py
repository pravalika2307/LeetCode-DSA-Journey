# LeetCode: 448
# Title: Find All Numbers Disappeared in an Array
# Difficulty: Easy
# Pattern: In-Place Cyclic Marking
# Time Complexity: O(n)
# Space Complexity: O(1) auxiliary

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        return [idx + 1 for idx, value in enumerate(nums) if value > 0]
