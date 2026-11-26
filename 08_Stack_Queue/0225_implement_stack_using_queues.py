# LeetCode: 225
# Title: Implement Stack using Queues
# Difficulty: Easy
# Pattern: Stack & Queue Design
# Time Complexity: O(n) for push, O(1) for pop/top
# Space Complexity: O(n)

from collections import deque


class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
