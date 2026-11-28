# Stack & Queue Patterns

Notes and common templates for Stack and Queue problems in Python.

---

## 1. Core Principles

- **Stack (LIFO):** Last In, First Out. Ideal for tracking nested structures, undo operations, matching pairs, and monotonic sequences.
- **Queue (FIFO):** First In, First Out. Standard for Breadth-First Search (BFS) and order processing.
- In Python, use `list` for stack (`append` / `pop`) and `collections.deque` for queue (`append` / `popleft`).

---

## 2. Monotonic Stack Pattern

Used when you need to find the **next greater** or **next smaller** element in $O(n)$ time.

### Monotonic Decreasing Stack Template (Next Greater Element)
```python
def next_greater_elements(nums):
    n = len(nums)
    res = [-1] * n
    stack = []  # stores indices

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            prev_idx = stack.pop()
            res[prev_idx] = nums[i]
        stack.append(i)
    return res
```

### Common Variations
- **Circular Arrays (LeetCode 503):** Loop up to `2 * n` and use `i % n`.
- **Daily Temperatures (LeetCode 739):** Store indices to compute distance `i - prev_idx`.
- **Largest Rectangle in Histogram (LeetCode 84):** Maintain increasing heights to find left/right boundary widths.

---

## 3. Two-Stack & Design Patterns

### Min Stack (LeetCode 155)
Maintain a primary stack alongside a secondary `min_stack` to achieve $O(1)$ `getMin()`:
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        cur_min = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(cur_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

### Queue using Stacks (LeetCode 232)
Amortized $O(1)$ operations by using two stacks (`in_stack` and `out_stack`). Transfer elements only when `out_stack` is empty.

---

## 4. Expression Parsing & Decoding

- **Simplify Path (LeetCode 71):** Split path by `/` and treat `..` as `stack.pop()`.
- **Reverse Polish Notation (LeetCode 150):** Push operands to stack; when operator arrives, pop two, evaluate, and push result back.
- **Decode String (LeetCode 394):** Store `(prev_string, repeat_count)` on bracket entry `[` and concatenate on exit `]`.
