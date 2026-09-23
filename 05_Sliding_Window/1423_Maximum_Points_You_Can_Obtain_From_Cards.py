# LeetCode: 1423
# Title: Maximum Points You Can Obtain from Cards
# Difficulty: Medium
# Pattern: Sliding Window (Fixed Complement)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        window_len = n - k
        if window_len == 0:
            return total

        window_sum = sum(cardPoints[:window_len])
        min_window = window_sum

        for right in range(window_len, n):
            window_sum += cardPoints[right] - cardPoints[right - window_len]
            if window_sum < min_window:
                min_window = window_sum

        return total - min_window
