# LeetCode: 66
# Title: Plus One
# Difficulty: Easy
# Pattern: Array Math / Carry Propagation
# Time Complexity: O(n)
# Space Complexity: O(1) auxiliary

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for idx in range(len(digits) - 1, -1, -1):
            if digits[idx] < 9:
                digits[idx] += 1
                return digits
            digits[idx] = 0

        return [1] + digits
