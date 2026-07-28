# LeetCode: 884
# Title: Uncommon Words from Two Sentences
# Difficulty: Easy
# Pattern: Hashing (Frequency Counting)
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        counts = Counter(s1.split()) + Counter(s2.split())
        return [word for word, freq in counts.items() if freq == 1]
