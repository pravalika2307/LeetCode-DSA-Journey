# LeetCode: 605
# Title: Can Place Flowers
# Difficulty: Easy
# Pattern: Greedy Array Scan
# Time Complexity: O(m)
# Space Complexity: O(1)

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        planted = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                left_empty = i == 0 or flowerbed[i - 1] == 0
                right_empty = i == length - 1 or flowerbed[i + 1] == 0
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    planted += 1
                    if planted >= n:
                        return True

        return planted >= n
