# LeetCode: 41
# Title: First Missing Positive
# Difficulty: Hard
# Pattern: Cyclic Sort / In-Place Index Placement
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            correct_idx = nums[i] - 1
            if 1 <= nums[i] <= n and nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        for idx in range(n):
            if nums[idx] != idx + 1:
                return idx + 1

        return n + 1
