# LeetCode: 26
# Title: Remove Duplicates from Sorted Array
# Difficulty: Easy
# Pattern: Two Pointers (In-Place)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1
        return write
