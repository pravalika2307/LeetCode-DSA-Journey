# LeetCode: 76
# Title: Minimum Window Substring
# Difficulty: Hard
# Pattern: Sliding Window (Variable) + Hash Map
# Time Complexity: O(n + m)
# Space Complexity: O(m)

from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        needed = Counter(t)
        required = len(needed)
        window = defaultdict(int)
        formed = 0

        best_len = float("inf")
        best_range = (0, 0)
        left = 0

        for right, ch in enumerate(s):
            window[ch] += 1
            if ch in needed and window[ch] == needed[ch]:
                formed += 1

            while left <= right and formed == required:
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_range = (left, right + 1)

                left_ch = s[left]
                window[left_ch] -= 1
                if left_ch in needed and window[left_ch] < needed[left_ch]:
                    formed -= 1
                left += 1

        if best_len == float("inf"):
            return ""
        return s[best_range[0] : best_range[1]]
