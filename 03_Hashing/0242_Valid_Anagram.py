# LeetCode: 242
# Title: Valid Anagram
# Difficulty: Easy
# Pattern: Hashing (Frequency Counting)
# Time Complexity: O(n)
# Space Complexity: O(1)

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
