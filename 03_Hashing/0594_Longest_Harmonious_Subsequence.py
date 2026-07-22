# LeetCode: 594
# Title: Longest Harmonious Subsequence
# Difficulty: Easy
# Pattern: Hashing (Frequency Counter)
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)
        best = 0

        for num, freq in counts.items():
            if num + 1 in counts:
                best = max(best, freq + counts[num + 1])

        return best
