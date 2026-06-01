# LeetCode: 229
# Title: Majority Element II
# Difficulty: Medium
# Pattern: Boyer-Moore Voting Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2 = None, None
        cnt1, cnt2 = 0, 0

        for num in nums:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1, cnt1 = num, 1
            elif cnt2 == 0:
                cand2, cnt2 = num, 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        result = []
        threshold = len(nums) // 3
        for cand in (cand1, cand2):
            if cand is not None and nums.count(cand) > threshold:
                result.append(cand)
        return result
