# LeetCode: 1207
# Title: Unique Number of Occurrences
# Difficulty: Easy
# Pattern: Hashing (Hash Map + Hash Set)
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequencies = Counter(arr).values()
        return len(frequencies) == len(set(frequencies))
