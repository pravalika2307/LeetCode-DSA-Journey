# LeetCode: 2269
# Title: Find the K-Beauty of a Number
# Difficulty: Easy
# Pattern: Sliding Window (Fixed)
# Time Complexity: O(d)
# Space Complexity: O(d)


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        text = str(num)
        count = 0

        for i in range(len(text) - k + 1):
            sub_val = int(text[i : i + k])
            if sub_val != 0 and num % sub_val == 0:
                count += 1

        return count
