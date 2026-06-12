# LeetCode: 493
# Title: Reverse Pairs
# Difficulty: Hard
# Pattern: Merge Sort / Divide and Conquer
# Time Complexity: O(n log n)
# Space Complexity: O(n)

from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def sort_and_count(left: int, right: int) -> int:
            if right - left <= 1:
                return 0

            mid = (left + right) // 2
            count = sort_and_count(left, mid) + sort_and_count(mid, right)

            j = mid
            for i in range(left, mid):
                while j < right and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - mid

            merged = []
            p1, p2 = left, mid
            while p1 < mid and p2 < right:
                if nums[p1] <= nums[p2]:
                    merged.append(nums[p1])
                    p1 += 1
                else:
                    merged.append(nums[p2])
                    p2 += 1
            merged.extend(nums[p1:mid])
            merged.extend(nums[p2:right])
            nums[left:right] = merged

            return count

        return sort_and_count(0, len(nums))
