# LeetCode: 167
# Title: Two Sum II - Input Array Is Sorted
# Difficulty: Medium
# Pattern: Two Pointers (Opposite Ends)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            if total < target:
                left += 1
            else:
                right -= 1

        return []
