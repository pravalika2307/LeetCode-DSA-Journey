# LeetCode: 438
# Title: Find All Anagrams in a String
# Difficulty: Medium
# Pattern: Sliding Window (Fixed) + Frequency Array
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        p_counts = [0] * 26
        window_counts = [0] * 26
        k = len(p)

        for i in range(k):
            p_counts[ord(p[i]) - ord("a")] += 1
            window_counts[ord(s[i]) - ord("a")] += 1

        result = [0] if window_counts == p_counts else []

        for right in range(k, len(s)):
            window_counts[ord(s[right]) - ord("a")] += 1
            window_counts[ord(s[right - k]) - ord("a")] -= 1
            if window_counts == p_counts:
                result.append(right - k + 1)

        return result
