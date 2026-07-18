# LeetCode: 532
# Title: K-diff Pairs in an Array
# Difficulty: Medium
# Pattern: Hashing (Frequency Counter)
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        counts = Counter(nums)
        pairs = 0

        for num, freq in counts.items():
            if k == 0:
                if freq > 1:
                    pairs += 1
            elif num + k in counts:
                pairs += 1

        return pairs
