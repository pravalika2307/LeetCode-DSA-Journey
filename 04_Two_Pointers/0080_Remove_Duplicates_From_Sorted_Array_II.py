# LeetCode: 80
# Title: Remove Duplicates from Sorted Array II
# Difficulty: Medium
# Pattern: Two Pointers (In-Place)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        write = 2
        for read in range(2, len(nums)):
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1

        return write
