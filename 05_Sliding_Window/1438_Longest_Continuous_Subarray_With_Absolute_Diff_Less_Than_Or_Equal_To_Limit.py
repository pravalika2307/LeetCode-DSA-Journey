# LeetCode: 1438
# Title: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# Difficulty: Medium
# Pattern: Sliding Window + Monotonic Deques
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_dq: deque[int] = deque()
        min_dq: deque[int] = deque()
        left = 0
        best = 0

        for right, val in enumerate(nums):
            while max_dq and nums[max_dq[-1]] < val:
                max_dq.pop()
            max_dq.append(right)

            while min_dq and nums[min_dq[-1]] > val:
                min_dq.pop()
            min_dq.append(right)

            while nums[max_dq[0]] - nums[min_dq[0]] > limit:
                left += 1
                if max_dq[0] < left:
                    max_dq.popleft()
                if min_dq[0] < left:
                    min_dq.popleft()

            length = right - left + 1
            if length > best:
                best = length

        return best
