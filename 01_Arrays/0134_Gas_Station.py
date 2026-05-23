# LeetCode: 134
# Title: Gas Station
# Difficulty: Medium
# Pattern: Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        tank = 0
        start = 0

        for idx in range(len(gas)):
            tank += gas[idx] - cost[idx]
            if tank < 0:
                tank = 0
                start = idx + 1

        return start
