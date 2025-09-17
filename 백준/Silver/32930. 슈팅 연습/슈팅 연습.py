import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
current = [tuple(map(int, input().split())) for _ in range(n)]
upcoming = deque(tuple(map(int, input().split())) for _ in range(m))

cx, cy = 0, 0
total = 0

for _ in range(m):
    max_idx = -1
    max_d2 = -1
    for i, (x, y) in enumerate(current):
        dx, dy = x - cx, y - cy
        d2 = dx*dx + dy*dy
        if d2 > max_d2:
            max_d2 = d2
            max_idx = i

    total += max_d2
    cx, cy = current[max_idx]

    current.pop(max_idx)

    if upcoming:
        current.append(upcoming.popleft())

print(total)
