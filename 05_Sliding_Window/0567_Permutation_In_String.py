# LeetCode: 567
# Title: Permutation in String
# Difficulty: Medium
# Pattern: Sliding Window (Fixed) + Frequency Array
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counts = [0] * 26
        window_counts = [0] * 26
        k = len(s1)

        for i in range(k):
            s1_counts[ord(s1[i]) - ord("a")] += 1
            window_counts[ord(s2[i]) - ord("a")] += 1

        if window_counts == s1_counts:
            return True

        for right in range(k, len(s2)):
            window_counts[ord(s2[right]) - ord("a")] += 1
            window_counts[ord(s2[right - k]) - ord("a")] -= 1
            if window_counts == s1_counts:
                return True

        return False
