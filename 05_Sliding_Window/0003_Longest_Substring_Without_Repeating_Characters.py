# LeetCode: 3
# Title: Longest Substring Without Repeating Characters
# Difficulty: Medium
# Pattern: Sliding Window (Variable) + Hash Map
# Time Complexity: O(n)
# Space Complexity: O(min(n, m))


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        best = 0

        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            length = right - left + 1
            if length > best:
                best = length

        return best
