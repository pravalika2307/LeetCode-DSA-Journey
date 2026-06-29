# LeetCode: 49
# Title: Group Anagrams
# Difficulty: Medium
# Pattern: Hashing (Character Frequency Key)
# Time Complexity: O(n * k)
# Space Complexity: O(n * k)

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            counts = [0] * 26
            for ch in word:
                counts[ord(ch) - ord("a")] += 1
            groups[tuple(counts)].append(word)

        return list(groups.values())
