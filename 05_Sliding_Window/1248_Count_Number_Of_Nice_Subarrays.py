# LeetCode: 1248
# Title: Count Number of Nice Subarrays
# Difficulty: Medium
# Pattern: Sliding Window (At Most K Difference)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def count_at_most(odd_limit: int) -> int:
            if odd_limit < 0:
                return 0
            left = 0
            odds = 0
            total = 0
            for right, val in enumerate(nums):
                if val % 2 == 1:
                    odds += 1
                while odds > odd_limit:
                    if nums[left] % 2 == 1:
                        odds -= 1
                    left += 1
                total += right - left + 1
            return total

        return count_at_most(k) - count_at_most(k - 1)
