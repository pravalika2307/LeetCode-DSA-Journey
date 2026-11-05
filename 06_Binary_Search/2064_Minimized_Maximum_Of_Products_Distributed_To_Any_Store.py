# LeetCode: 2064
# Title: Minimized Maximum of Products Distributed to Any Store
# Difficulty: Medium
# Pattern: Binary Search on Answer
# Time Complexity: O(m log(max(quantities)))
# Space Complexity: O(1)

from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(limit: int) -> bool:
            stores = 0
            for qty in quantities:
                stores += (qty + limit - 1) // limit
            return stores <= n

        left, right = 1, max(quantities)
        while left < right:
            mid = left + (right - left) // 2
            if can_distribute(mid):
                right = mid
            else:
                left = mid + 1

        return left
