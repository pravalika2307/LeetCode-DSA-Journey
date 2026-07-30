# LeetCode: 1002
# Title: Find Common Characters
# Difficulty: Easy
# Pattern: Hashing (Frequency Intersection)
# Time Complexity: O(n * k)
# Space Complexity: O(1)

from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        min_freq = [float("inf")] * 26
        for word in words:
            current = [0] * 26
            for ch in word:
                current[ord(ch) - ord("a")] += 1
            for idx in range(26):
                if current[idx] < min_freq[idx]:
                    min_freq[idx] = current[idx]

        result = []
        for idx in range(26):
            if min_freq[idx] > 0:
                result.extend([chr(ord("a") + idx)] * int(min_freq[idx]))
        return result
