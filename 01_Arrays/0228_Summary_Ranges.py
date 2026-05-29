# LeetCode: 228
# Title: Summary Ranges
# Difficulty: Easy
# Pattern: Array Linear Scan
# Time Complexity: O(n)
# Space Complexity: O(1) auxiliary

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges: List[str] = []
        i = 0
        n = len(nums)

        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            if nums[i] == start:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}->{nums[i]}")
            i += 1

        return ranges
