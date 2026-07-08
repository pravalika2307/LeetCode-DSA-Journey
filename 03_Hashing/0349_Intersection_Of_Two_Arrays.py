# LeetCode: 349
# Title: Intersection of Two Arrays
# Difficulty: Easy
# Pattern: Hashing (Hash Set)
# Time Complexity: O(n + m)
# Space Complexity: O(min(n, m))

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        lookup = set(nums1)
        result = []

        for num in nums2:
            if num in lookup:
                result.append(num)
                lookup.remove(num)

        return result
