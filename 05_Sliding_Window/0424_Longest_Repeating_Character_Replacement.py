# LeetCode: 424
# Title: Longest Repeating Character Replacement
# Difficulty: Medium
# Pattern: Sliding Window (Variable) + Frequency Array
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        left = 0
        max_freq = 0
        best = 0

        for right, ch in enumerate(s):
            idx = ord(ch) - ord("A")
            counts[idx] += 1
            if counts[idx] > max_freq:
                max_freq = counts[idx]

            while (right - left + 1) - max_freq > k:
                counts[ord(s[left]) - ord("A")] -= 1
                left += 1

            length = right - left + 1
            if length > best:
                best = length

        return best
