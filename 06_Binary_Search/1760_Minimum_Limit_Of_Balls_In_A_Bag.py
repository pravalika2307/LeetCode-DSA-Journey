# LeetCode: 1760
# Title: Minimum Limit of Balls in a Bag
# Difficulty: Medium
# Pattern: Binary Search on Answer
# Time Complexity: O(n log(max(nums)))
# Space Complexity: O(1)

from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def can_achieve(penalty: int) -> bool:
            ops = 0
            for bag in nums:
                ops += (bag - 1) // penalty
            return ops <= maxOperations

        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if can_achieve(mid):
                right = mid
            else:
                left = mid + 1

        return left
