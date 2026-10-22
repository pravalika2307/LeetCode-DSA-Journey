# LeetCode: 658
# Title: Find K Closest Elements
# Difficulty: Medium
# Pattern: Binary Search (Window Start Search)
# Time Complexity: O(log(n - k) + k)
# Space Complexity: O(1) auxiliary

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k

        while left < right:
            mid = left + (right - left) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left : left + k]
