# LeetCode: 475
# Title: Heaters
# Difficulty: Medium
# Pattern: Two Pointers + Sorting
# Time Complexity: O(n log n + m log m)
# Space Complexity: O(1) auxiliary

from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radius = 0
        h_idx = 0

        for house in houses:
            while h_idx + 1 < len(heaters) and abs(heaters[h_idx + 1] - house) <= abs(
                heaters[h_idx] - house
            ):
                h_idx += 1
            dist = abs(heaters[h_idx] - house)
            if dist > radius:
                radius = dist

        return radius
