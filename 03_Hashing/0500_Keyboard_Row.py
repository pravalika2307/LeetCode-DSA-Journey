# LeetCode: 500
# Title: Keyboard Row
# Difficulty: Easy
# Pattern: Hashing (Hash Set)
# Time Complexity: O(total chars)
# Space Complexity: O(1)

from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        result: List[str] = []

        for word in words:
            lower_chars = set(word.lower())
            if any(lower_chars <= row for row in rows):
                result.append(word)

        return result
