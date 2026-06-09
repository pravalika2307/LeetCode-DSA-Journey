# LeetCode: 442
# Title: Find All Duplicates in an Array
# Difficulty: Medium
# Pattern: In-Place Cyclic Marking
# Time Complexity: O(n)
# Space Complexity: O(1) auxiliary

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates: List[int] = []

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                duplicates.append(idx + 1)
            else:
                nums[idx] = -nums[idx]

        return duplicates
