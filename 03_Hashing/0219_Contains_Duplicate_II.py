# LeetCode: 219
# Title: Contains Duplicate II
# Difficulty: Easy
# Pattern: Hashing (Last Seen Index)
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for idx, num in enumerate(nums):
            if num in last_seen and idx - last_seen[num] <= k:
                return True
            last_seen[num] = idx

        return False
