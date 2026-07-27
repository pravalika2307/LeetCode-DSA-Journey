# LeetCode: 791
# Title: Custom Sort String
# Difficulty: Medium
# Pattern: Hashing (Frequency Counting)
# Time Complexity: O(n + m)
# Space Complexity: O(n)

from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        parts = []

        for ch in order:
            if ch in counts:
                parts.append(ch * counts.pop(ch))

        for ch, freq in counts.items():
            parts.append(ch * freq)

        return "".join(parts)
