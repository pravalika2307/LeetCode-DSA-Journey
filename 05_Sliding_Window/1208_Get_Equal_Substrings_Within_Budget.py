# LeetCode: 1208
# Title: Get Equal Substrings Within Budget
# Difficulty: Medium
# Pattern: Sliding Window (Variable)
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        current_cost = 0
        best = 0

        for right in range(len(s)):
            current_cost += abs(ord(s[right]) - ord(t[right]))
            while current_cost > maxCost:
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            length = right - left + 1
            if length > best:
                best = length

        return best
