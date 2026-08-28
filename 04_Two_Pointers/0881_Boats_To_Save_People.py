# LeetCode: 881
# Title: Boats to Save People
# Difficulty: Medium
# Pattern: Two Pointers + Greedy Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(1) auxiliary

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1

        return boats
