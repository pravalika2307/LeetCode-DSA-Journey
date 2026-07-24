# LeetCode: 771
# Title: Jewels and Stones
# Difficulty: Easy
# Pattern: Hashing (Hash Set)
# Time Complexity: O(J + S)
# Space Complexity: O(J)


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        return sum(1 for stone in stones if stone in jewel_set)
