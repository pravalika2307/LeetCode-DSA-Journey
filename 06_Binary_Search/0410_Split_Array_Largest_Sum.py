# LeetCode: 410
# Title: Split Array Largest Sum
# Difficulty: Hard
# Pattern: Binary Search on Answer
# Time Complexity: O(n log(sum(nums)))
# Space Complexity: O(1)

from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum: int) -> bool:
            subarrays = 1
            current = 0
            for val in nums:
                if current + val > max_sum:
                    subarrays += 1
                    current = 0
                current += val
            return subarrays <= k

        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1

        return left
