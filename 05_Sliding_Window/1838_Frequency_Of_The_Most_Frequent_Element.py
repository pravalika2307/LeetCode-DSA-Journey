# LeetCode: 1838
# Title: Frequency of the Most Frequent Element
# Difficulty: Medium
# Pattern: Sliding Window (Variable) + Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(1) auxiliary

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        window_sum = 0
        best = 1

        for right, target in enumerate(nums):
            window_sum += target
            while target * (right - left + 1) - window_sum > k:
                window_sum -= nums[left]
                left += 1
            length = right - left + 1
            if length > best:
                best = length

        return best
