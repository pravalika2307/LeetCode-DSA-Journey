# LeetCode: 27
# Title: Remove Element
# Difficulty: Easy
# Pattern: Two Pointers (In-Place)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        for value in nums:
            if value != val:
                nums[write] = value
                write += 1
        return write
