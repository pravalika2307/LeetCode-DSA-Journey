# LeetCode: 2444
# Title: Count Subarrays With Fixed Bounds
# Difficulty: Hard
# Pattern: Sliding Window (Last-Seen Bound Tracking)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        bad_idx = -1
        last_min = -1
        last_max = -1
        total = 0

        for idx, val in enumerate(nums):
            if val < minK or val > maxK:
                bad_idx = idx
            if val == minK:
                last_min = idx
            if val == maxK:
                last_max = idx

            valid_start = min(last_min, last_max)
            if valid_start > bad_idx:
                total += valid_start - bad_idx

        return total
