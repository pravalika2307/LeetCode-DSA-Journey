# LeetCode: 383
# Title: Ransom Note
# Difficulty: Easy
# Pattern: Hashing (Frequency Counting)
# Time Complexity: O(n + m)
# Space Complexity: O(1)

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        available = Counter(magazine)
        for ch in ransomNote:
            if available[ch] == 0:
                return False
            available[ch] -= 1

        return True
