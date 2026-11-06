# LeetCode: 2300
# Title: Successful Pairs of Spells and Potions
# Difficulty: Medium
# Pattern: Binary Search + Sorting
# Time Complexity: O((n + m) log m)
# Space Complexity: O(1) auxiliary

from bisect import bisect_left
from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        m = len(potions)
        pairs: List[int] = []

        for spell in spells:
            min_potion = (success + spell - 1) // spell
            idx = bisect_left(potions, min_potion)
            pairs.append(m - idx)

        return pairs
