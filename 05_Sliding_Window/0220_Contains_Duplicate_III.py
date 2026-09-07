# LeetCode: 220
# Title: Contains Duplicate III
# Difficulty: Hard
# Pattern: Sliding Window + Bucketing
# Time Complexity: O(n)
# Space Complexity: O(min(n, indexDiff))

from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        if valueDiff < 0 or indexDiff <= 0:
            return False

        bucket_size = valueDiff + 1
        buckets: dict[int, int] = {}

        for idx, num in enumerate(nums):
            bucket_id = num // bucket_size
            if bucket_id in buckets:
                return True
            if bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
            if bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True

            buckets[bucket_id] = num
            if idx >= indexDiff:
                old_bucket = nums[idx - indexDiff] // bucket_size
                del buckets[old_bucket]

        return False
