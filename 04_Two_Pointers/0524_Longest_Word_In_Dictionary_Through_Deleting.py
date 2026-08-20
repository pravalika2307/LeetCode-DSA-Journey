# LeetCode: 524
# Title: Longest Word in Dictionary through Deleting
# Difficulty: Medium
# Pattern: Two Pointers (Subsequence Matching)
# Time Complexity: O(d * (n + k))
# Space Complexity: O(1) auxiliary

from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(word: str) -> bool:
            i = 0
            for ch in s:
                if i < len(word) and ch == word[i]:
                    i += 1
            return i == len(word)

        best = ""
        for word in dictionary:
            if len(word) > len(best) or (len(word) == len(best) and word < best):
                if is_subsequence(word):
                    best = word

        return best
