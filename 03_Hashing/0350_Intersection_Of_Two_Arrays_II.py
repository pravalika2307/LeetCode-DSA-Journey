# LeetCode: 350
# Title: Intersection of Two Arrays II
# Difficulty: Easy
# Pattern: Hashing (Frequency Counter)
# Time Complexity: O(n + m)
# Space Complexity: O(min(n, m))

from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        counts = Counter(nums1)
        result = []

        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result
