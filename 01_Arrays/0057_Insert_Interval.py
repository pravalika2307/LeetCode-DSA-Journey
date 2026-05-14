# LeetCode: 57
# Title: Insert Interval
# Difficulty: Medium
# Pattern: Interval Merging
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result: List[List[int]] = []
        i = 0
        n = len(intervals)
        new_start, new_end = newInterval

        while i < n and intervals[i][1] < new_start:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        result.append([new_start, new_end])

        while i < n:
            result.append(intervals[i])
            i += 1

        return result
