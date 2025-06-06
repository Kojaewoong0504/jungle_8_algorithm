import sys

input = sys.stdin.readline
from collections import deque

v, r, c = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(r)]
time = [[float('inf')] * c for _ in range(r)]
time[0][0] = 0

q = deque()
q.append((0, 0, v))
while q:
    nr, nc, speed = q.popleft()
    for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        sr, sc = nr + dr, nc + dc
        if not (0 <= sr < r and 0 <= sc < c):
            continue
        if time[sr][sc] <= time[nr][nc] + (1 / speed):
            continue
        time[sr][sc] = time[nr][nc] + (1 / speed)
        speed_new = speed * (2 ** (mat[nr][nc] - mat[sr][sc]))
        q.append((sr, sc, speed_new))

print(f'{time[r - 1][c - 1]:.2f}')
