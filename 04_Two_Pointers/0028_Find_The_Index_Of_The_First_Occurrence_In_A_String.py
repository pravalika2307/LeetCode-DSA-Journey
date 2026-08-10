# LeetCode: 28
# Title: Find the Index of the First Occurrence in a String
# Difficulty: Easy
# Pattern: Two Pointers / String Matching
# Time Complexity: O(n * m)
# Space Complexity: O(1)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        n, m = len(haystack), len(needle)
        for start in range(n - m + 1):
            idx = 0
            while idx < m and haystack[start + idx] == needle[idx]:
                idx += 1
            if idx == m:
                return start

        return -1
