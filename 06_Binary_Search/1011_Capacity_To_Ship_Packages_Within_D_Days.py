# LeetCode: 1011
# Title: Capacity To Ship Packages Within D Days
# Difficulty: Medium
# Pattern: Binary Search on Answer
# Time Complexity: O(n log(sum(weights)))
# Space Complexity: O(1)

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity: int) -> bool:
            required_days = 1
            current_load = 0
            for weight in weights:
                if current_load + weight > capacity:
                    required_days += 1
                    current_load = 0
                current_load += weight
            return required_days <= days

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1

        return left
