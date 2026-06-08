# LeetCode: 414
# Title: Third Maximum Number
# Difficulty: Easy
# Pattern: Array Linear Scan
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List, Optional


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first: Optional[int] = None
        second: Optional[int] = None
        third: Optional[int] = None

        for num in nums:
            if num in (first, second, third):
                continue
            if first is None or num > first:
                third, second, first = second, first, num
            elif second is None or num > second:
                third, second = second, num
            elif third is None or num > third:
                third = num

        return third if third is not None else first  # type: ignore[return-value]
