# LeetCode: 56
# Title: Merge Intervals
# Difficulty: Medium
# Pattern: Sorting + Interval Merging
# Time Complexity: O(n log n)
# Space Complexity: O(n)

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda interval: interval[0])
        merged: List[List[int]] = [intervals[0][:]]

        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                if end > merged[-1][1]:
                    merged[-1][1] = end
            else:
                merged.append([start, end])

        return merged
