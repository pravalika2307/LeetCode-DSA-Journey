# LeetCode: 387
# Title: First Unique Character in a String
# Difficulty: Easy
# Pattern: Hashing (Frequency Counting)
# Time Complexity: O(n)
# Space Complexity: O(1)

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for idx, ch in enumerate(s):
            if counts[ch] == 1:
                return idx
        return -1
