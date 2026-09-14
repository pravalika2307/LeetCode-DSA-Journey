# LeetCode: 904
# Title: Fruit Into Baskets
# Difficulty: Medium
# Pattern: Sliding Window (At Most 2 Distinct)
# Time Complexity: O(n)
# Space Complexity: O(1)

from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts = defaultdict(int)
        left = 0
        best = 0

        for right, fruit in enumerate(fruits):
            counts[fruit] += 1
            while len(counts) > 2:
                left_fruit = fruits[left]
                counts[left_fruit] -= 1
                if counts[left_fruit] == 0:
                    del counts[left_fruit]
                left += 1

            length = right - left + 1
            if length > best:
                best = length

        return best
