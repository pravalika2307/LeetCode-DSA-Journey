# LeetCode: 1160
# Title: Find Words That Can Be Formed by Characters
# Difficulty: Easy
# Pattern: Hashing (Frequency Counting)
# Time Complexity: O(total chars)
# Space Complexity: O(1)

from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        available = Counter(chars)
        total_len = 0

        for word in words:
            word_counts = Counter(word)
            if all(word_counts[ch] <= available[ch] for ch in word_counts):
                total_len += len(word)

        return total_len
