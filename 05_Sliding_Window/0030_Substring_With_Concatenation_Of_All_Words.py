# LeetCode: 30
# Title: Substring with Concatenation of All Words
# Difficulty: Hard
# Pattern: Sliding Window (Word-Length Offset) + Hash Map
# Time Complexity: O(n * word_len)
# Space Complexity: O(k * word_len)

from collections import Counter, defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        if len(s) < total_len:
            return []

        needed = Counter(words)
        result: List[int] = []

        for offset in range(word_len):
            left = offset
            window = defaultdict(int)
            matched_words = 0

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right : right + word_len]
                if word not in needed:
                    window.clear()
                    matched_words = 0
                    left = right + word_len
                    continue

                window[word] += 1
                matched_words += 1

                while window[word] > needed[word]:
                    left_word = s[left : left + word_len]
                    window[left_word] -= 1
                    matched_words -= 1
                    left += word_len

                if matched_words == word_count:
                    result.append(left)

        return result
