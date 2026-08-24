# LeetCode: 557
# Title: Reverse Words in a String III
# Difficulty: Easy
# Pattern: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        n = len(chars)
        start = 0

        for idx in range(n + 1):
            if idx == n or chars[idx] == " ":
                left, right = start, idx - 1
                while left < right:
                    chars[left], chars[right] = chars[right], chars[left]
                    left += 1
                    right -= 1
                start = idx + 1

        return "".join(chars)
