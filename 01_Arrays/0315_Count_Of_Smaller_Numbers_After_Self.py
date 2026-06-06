# LeetCode: 315
# Title: Count of Smaller Numbers After Self
# Difficulty: Hard
# Pattern: Merge Sort / Divide and Conquer
# Time Complexity: O(n log n)
# Space Complexity: O(n)

from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        indexed = list(enumerate(nums))

        def merge_sort(arr: List[tuple[int, int]]) -> List[tuple[int, int]]:
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            merged: List[tuple[int, int]] = []
            i = j = 0
            right_smaller = 0

            while i < len(left) and j < len(right):
                if right[j][1] < left[i][1]:
                    right_smaller += 1
                    merged.append(right[j])
                    j += 1
                else:
                    counts[left[i][0]] += right_smaller
                    merged.append(left[i])
                    i += 1

            while i < len(left):
                counts[left[i][0]] += right_smaller
                merged.append(left[i])
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        merge_sort(indexed)
        return counts
