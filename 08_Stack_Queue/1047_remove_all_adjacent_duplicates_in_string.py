# LeetCode: 1047
# Title: Remove All Adjacent Duplicates In String
# Difficulty: Easy
# Pattern: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
