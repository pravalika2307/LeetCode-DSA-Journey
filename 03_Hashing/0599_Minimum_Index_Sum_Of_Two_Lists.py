# LeetCode: 599
# Title: Minimum Index Sum of Two Lists
# Difficulty: Easy
# Pattern: Hashing (Index Map)
# Time Complexity: O(n + m)
# Space Complexity: O(n)

from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {name: idx for idx, name in enumerate(list1)}
        min_sum = float("inf")
        result: List[str] = []

        for idx2, name in enumerate(list2):
            if name in index_map:
                total = idx2 + index_map[name]
                if total < min_sum:
                    min_sum = total
                    result = [name]
                elif total == min_sum:
                    result.append(name)

        return result
