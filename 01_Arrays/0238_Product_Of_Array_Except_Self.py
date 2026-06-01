# LeetCode: 238
# Title: Product of Array Except Self
# Difficulty: Medium
# Pattern: Prefix and Suffix Products
# Time Complexity: O(n)
# Space Complexity: O(1) auxiliary

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for idx in range(n):
            answer[idx] = prefix
            prefix *= nums[idx]

        suffix = 1
        for idx in range(n - 1, -1, -1):
            answer[idx] *= suffix
            suffix *= nums[idx]

        return answer
