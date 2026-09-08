# LeetCode: 239
# Title: Sliding Window Maximum
# Difficulty: Hard
# Pattern: Sliding Window + Monotonic Deque
# Time Complexity: O(n)
# Space Complexity: O(k)

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []

        dq: deque[int] = deque()
        result: List[int] = []

        for idx, value in enumerate(nums):
            while dq and dq[0] <= idx - k:
                dq.popleft()
            while dq and nums[dq[-1]] <= value:
                dq.pop()
            dq.append(idx)

            if idx >= k - 1:
                result.append(nums[dq[0]])

        return result
