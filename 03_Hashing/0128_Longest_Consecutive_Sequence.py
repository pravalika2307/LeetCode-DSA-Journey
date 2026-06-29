# LeetCode: 128
# Title: Longest Consecutive Sequence
# Difficulty: Medium
# Pattern: Hashing (Hash Set)
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                streak = 1
                while current + 1 in num_set:
                    current += 1
                    streak += 1
                if streak > longest:
                    longest = streak

        return longest
