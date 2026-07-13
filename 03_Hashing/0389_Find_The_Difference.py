# LeetCode: 389
# Title: Find the Difference
# Difficulty: Easy
# Pattern: Bit Manipulation (XOR) / Hashing
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor_val = 0
        for ch in s:
            xor_val ^= ord(ch)
        for ch in t:
            xor_val ^= ord(ch)
        return chr(xor_val)
