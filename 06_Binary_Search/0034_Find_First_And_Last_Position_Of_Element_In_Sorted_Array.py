# LeetCode: 34
# Title: Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
# Pattern: Binary Search (Lower and Upper Bounds)
# Time Complexity: O(log n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(find_first: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    bound = mid
                    if find_first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return bound

        first = find_bound(True)
        if first == -1:
            return [-1, -1]
        return [first, find_bound(False)]
