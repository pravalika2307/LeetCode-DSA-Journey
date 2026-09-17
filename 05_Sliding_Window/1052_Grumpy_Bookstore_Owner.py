# LeetCode: 1052
# Title: Grumpy Bookstore Owner
# Difficulty: Medium
# Pattern: Sliding Window (Fixed)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        base_satisfied = 0
        extra = 0
        best_extra = 0

        for right in range(len(customers)):
            if grumpy[right] == 0:
                base_satisfied += customers[right]
            else:
                extra += customers[right]

            if right >= minutes and grumpy[right - minutes] == 1:
                extra -= customers[right - minutes]

            if extra > best_extra:
                best_extra = extra

        return base_satisfied + best_extra
