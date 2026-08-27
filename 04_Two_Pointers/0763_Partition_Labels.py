# LeetCode: 763
# Title: Partition Labels
# Difficulty: Medium
# Pattern: Two Pointers / Greedy Intervals
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {ch: idx for idx, ch in enumerate(s)}
        partitions: List[int] = []
        start = 0
        end = 0

        for idx, ch in enumerate(s):
            if last_index[ch] > end:
                end = last_index[ch]
            if idx == end:
                partitions.append(end - start + 1)
                start = idx + 1

        return partitions
