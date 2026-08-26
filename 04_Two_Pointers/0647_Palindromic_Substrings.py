# LeetCode: 647
# Title: Palindromic Substrings
# Difficulty: Medium
# Pattern: Two Pointers (Expand Around Center)
# Time Complexity: O(n^2)
# Space Complexity: O(1)


class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        n = len(s)

        def count_palindromes(left: int, right: int) -> int:
            cnt = 0
            while left >= 0 and right < n and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
            return cnt

        for center in range(n):
            total += count_palindromes(center, center)
            total += count_palindromes(center, center + 1)

        return total
