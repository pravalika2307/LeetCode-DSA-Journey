# LeetCode: 692
# Title: Top K Frequent Words
# Difficulty: Medium
# Pattern: Hashing + Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(n)

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        sorted_words = sorted(counts.keys(), key=lambda w: (-counts[w], w))
        return sorted_words[:k]
