# LeetCode: 1358
# Title: Number of Substrings Containing All Three Characters
# Difficulty: Medium
# Pattern: Sliding Window (Variable)
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counts = [0, 0, 0]
        left = 0
        total = 0

        for right, ch in enumerate(s):
            counts[ord(ch) - ord("a")] += 1
            while counts[0] > 0 and counts[1] > 0 and counts[2] > 0:
                total += len(s) - right
                counts[ord(s[left]) - ord("a")] -= 1
                left += 1

        return total
