# LeetCode: 541
# Title: Reverse String II
# Difficulty: Easy
# Pattern: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        n = len(chars)

        for start in range(0, n, 2 * k):
            left = start
            right = min(start + k - 1, n - 1)
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        return "".join(chars)
