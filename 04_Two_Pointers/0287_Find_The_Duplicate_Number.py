# LeetCode: 287
# Title: Find the Duplicate Number
# Difficulty: Medium
# Pattern: Two Pointers (Floyd's Cycle Detection)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
