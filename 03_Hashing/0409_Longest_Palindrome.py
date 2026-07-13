# LeetCode: 409
# Title: Longest Palindrome
# Difficulty: Easy
# Pattern: Hashing (Frequency Counting)
# Time Complexity: O(n)
# Space Complexity: O(1)

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        has_odd = False

        for freq in counts.values():
            length += (freq // 2) * 2
            if freq % 2 == 1:
                has_odd = True

        return length + (1 if has_odd else 0)
