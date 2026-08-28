# LeetCode: 844
# Title: Backspace String Compare
# Difficulty: Easy
# Pattern: Two Pointers (Reverse Scan)
# Time Complexity: O(n + m)
# Space Complexity: O(1)


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def next_valid_index(text: str, idx: int) -> int:
            skip = 0
            while idx >= 0:
                if text[idx] == "#":
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    break
                idx -= 1
            return idx

        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            i = next_valid_index(s, i)
            j = next_valid_index(t, j)
            ch_s = s[i] if i >= 0 else ""
            ch_t = t[j] if j >= 0 else ""
            if ch_s != ch_t:
                return False
            i -= 1
            j -= 1

        return True
