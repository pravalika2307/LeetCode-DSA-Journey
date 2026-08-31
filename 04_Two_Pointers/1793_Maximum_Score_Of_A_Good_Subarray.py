# LeetCode: 1793
# Title: Maximum Score of a Good Subarray
# Difficulty: Hard
# Pattern: Two Pointers (Greedy Expansion)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = right = k
        cur_min = nums[k]
        best = nums[k]

        while left > 0 or right < n - 1:
            left_val = nums[left - 1] if left > 0 else -1
            right_val = nums[right + 1] if right < n - 1 else -1

            if left_val > right_val:
                left -= 1
                cur_min = min(cur_min, nums[left])
            else:
                right += 1
                cur_min = min(cur_min, nums[right])

            score = cur_min * (right - left + 1)
            if score > best:
                best = score

        return best
