# LeetCode: 202
# Title: Happy Number
# Difficulty: Easy
# Pattern: Hashing (Cycle Detection with Hash Set)
# Time Complexity: O(log n)
# Space Complexity: O(log n)


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            next_val = 0
            while n > 0:
                digit = n % 10
                next_val += digit * digit
                n //= 10
            n = next_val

        return n == 1
