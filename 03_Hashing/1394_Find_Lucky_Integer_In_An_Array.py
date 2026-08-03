# LeetCode: 1394
# Title: Find Lucky Integer in an Array
# Difficulty: Easy
# Pattern: Hashing (Frequency Counter)
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)
        best = -1
        for num, freq in counts.items():
            if num == freq and num > best:
                best = num
        return best
