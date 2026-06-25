# LeetCode: 1672
# Title: Richest Customer Wealth
# Difficulty: Easy
# Pattern: Matrix Row Sum
# Time Complexity: O(m * n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(customer) for customer in accounts)
