# LeetCode: 1898
# Title: Maximum Number of Removable Characters
# Difficulty: Medium
# Pattern: Binary Search on Answer + Two Pointers
# Time Complexity: O((|s| + |removable|) * log |removable|)
# Space Complexity: O(|removable|)

from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def is_subsequence(k: int) -> bool:
            removed = set(removable[:k])
            p_idx = 0
            for s_idx, ch in enumerate(s):
                if s_idx in removed:
                    continue
                if ch == p[p_idx]:
                    p_idx += 1
                    if p_idx == len(p):
                        return True
            return p_idx == len(p)

        left, right = 0, len(removable)
        best = 0

        while left <= right:
            mid = left + (right - left) // 2
            if is_subsequence(mid):
                best = mid
                left = mid + 1
            else:
                right = mid - 1

        return best
