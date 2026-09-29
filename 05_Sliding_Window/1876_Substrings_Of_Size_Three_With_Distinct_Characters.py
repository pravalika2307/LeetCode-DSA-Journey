# LeetCode: 1876
# Title: Substrings of Size Three with Distinct Characters
# Difficulty: Easy
# Pattern: Sliding Window (Fixed)
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 2):
            if s[i] != s[i + 1] and s[i] != s[i + 2] and s[i + 1] != s[i + 2]:
                count += 1
        return count
