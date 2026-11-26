# LeetCode: 71
# Title: Simplify Path
# Difficulty: Medium
# Pattern: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stack = []
        for part in parts:
            if part == '' or part == '.':
                continue
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)
