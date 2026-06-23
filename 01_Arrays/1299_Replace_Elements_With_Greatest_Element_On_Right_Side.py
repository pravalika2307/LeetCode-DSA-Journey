# LeetCode: 1299
# Title: Replace Elements with Greatest Element on Right Side
# Difficulty: Easy
# Pattern: Array Reverse Scan
# Time Complexity: O(n)
# Space Complexity: O(1) auxiliary

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = right_max
            if current > right_max:
                right_max = current
        return arr
