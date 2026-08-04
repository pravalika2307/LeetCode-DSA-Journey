# LeetCode: 5
# Title: Longest Palindromic Substring
# Difficulty: Medium
# Pattern: Two Pointers (Expand Around Center)
# Time Complexity: O(n^2)
# Space Complexity: O(1)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        start, end = 0, 0

        def expand(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for center in range(len(s)):
            l1, r1 = expand(center, center)
            if r1 - l1 > end - start:
                start, end = l1, r1

            l2, r2 = expand(center, center + 1)
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start : end + 1]
