# LeetCode: 1343
# Title: Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# Difficulty: Medium
# Pattern: Sliding Window (Fixed)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        window_sum = sum(arr[:k])
        count = 1 if window_sum >= target else 0

        for right in range(k, len(arr)):
            window_sum += arr[right] - arr[right - k]
            if window_sum >= target:
                count += 1

        return count
