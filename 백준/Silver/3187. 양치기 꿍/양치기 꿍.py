import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
vis = [[False] * C for _ in range(R)]

# 4방향 이동
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(sr, sc):
    q = deque()
    q.append((sr, sc))
    vis[sr][sc] = True

    sheep = 0
    wolf = 0
    if grid[sr][sc] == 'k':
        sheep += 1
    elif grid[sr][sc] == 'v':
        wolf += 1

    while q:
        r, c = q.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if not vis[nr][nc] and grid[nr][nc] != '#':
                    vis[nr][nc] = True
                    ch = grid[nr][nc]
                    if ch == 'k':
                        sheep += 1
                    elif ch == 'v':
                        wolf += 1
                    q.append((nr, nc))
    return sheep, wolf

total_sheep = 0
total_wolf = 0

for i in range(R):
    for j in range(C):
        if grid[i][j] != '#' and not vis[i][j]:
            s, w = bfs(i, j)
            if s > w:
                total_sheep += s
            else:
                total_wolf += w

print(total_sheep, total_wolf)
