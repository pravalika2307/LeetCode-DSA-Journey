# LeetCode: 289
# Title: Game of Life
# Difficulty: Medium
# Pattern: Matrix In-Place State Encoding
# Time Complexity: O(m * n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def live_neighbors(r: int, c: int) -> int:
            count = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in (1, 2):
                        count += 1
            return count

        # 2: live -> dead, 3: dead -> live
        for r in range(rows):
            for c in range(cols):
                neighbors = live_neighbors(r, c)
                if board[r][c] == 1 and (neighbors < 2 or neighbors > 3):
                    board[r][c] = 2
                elif board[r][c] == 0 and neighbors == 3:
                    board[r][c] = 3

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1
