# LeetCode: 451
# Title: Sort Characters By Frequency
# Difficulty: Medium
# Pattern: Hashing + Bucket Sort
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        buckets = [[] for _ in range(len(s) + 1)]

        for ch, freq in counts.items():
            buckets[freq].append(ch)

        parts = []
        for freq in range(len(s), 0, -1):
            for ch in buckets[freq]:
                parts.append(ch * freq)

        return "".join(parts)
