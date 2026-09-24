# LeetCode: 1456
# Title: Maximum Number of Vowels in a Substring of Given Length
# Difficulty: Medium
# Pattern: Sliding Window (Fixed)
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        current = 0
        best = 0

        for right, ch in enumerate(s):
            if ch in vowels:
                current += 1
            if right >= k and s[right - k] in vowels:
                current -= 1
            if current > best:
                best = current

        return best
