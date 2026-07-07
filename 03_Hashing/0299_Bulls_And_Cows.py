# LeetCode: 299
# Title: Bulls and Cows
# Difficulty: Medium
# Pattern: Hashing (Frequency Counting)
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        secret_counts = [0] * 10
        guess_counts = [0] * 10

        for s_ch, g_ch in zip(secret, guess):
            if s_ch == g_ch:
                bulls += 1
            else:
                secret_counts[int(s_ch)] += 1
                guess_counts[int(g_ch)] += 1

        cows = sum(min(secret_counts[d], guess_counts[d]) for d in range(10))
        return f"{bulls}A{cows}B"
