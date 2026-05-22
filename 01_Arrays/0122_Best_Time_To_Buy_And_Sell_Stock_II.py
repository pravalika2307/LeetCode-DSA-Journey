# LeetCode: 122
# Title: Best Time to Buy and Sell Stock II
# Difficulty: Medium
# Pattern: Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        for idx in range(1, len(prices)):
            if prices[idx] > prices[idx - 1]:
                total_profit += prices[idx] - prices[idx - 1]

        return total_profit
