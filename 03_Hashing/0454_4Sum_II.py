# LeetCode: 454
# Title: 4Sum II
# Difficulty: Medium
# Pattern: Hashing (Hash Map Pair Sums)
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

from collections import defaultdict
from typing import List


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        ab_sums = defaultdict(int)
        for a in nums1:
            for b in nums2:
                ab_sums[a + b] += 1

        tuples = 0
        for c in nums3:
            for d in nums4:
                tuples += ab_sums[-(c + d)]

        return tuples
