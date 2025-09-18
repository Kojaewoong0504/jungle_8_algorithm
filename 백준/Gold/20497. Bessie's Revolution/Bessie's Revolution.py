import sys
from collections import deque

input = sys.stdin.readline
N = int(input().strip())
grid = [list(input().strip()) for _ in range(N)]

def open_cell(r, c):
    return 0 <= r < N and 0 <= c < N and grid[r][c] == '.'

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

def neighbors(r, c):
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        if open_cell(nr, nc):
            yield (nr, nc)

def splits_if_block(r, c):
    nb = list(neighbors(r, c))
    if len(nb) < 2:
        return False

    a = nb[0]
    q = deque([a])
    seen = {a}

    while q:
        y, x = q.popleft()
        for dy, dx in dirs:
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < N:
                if (ny, nx) != (r, c) and grid[ny][nx] == '.' and (ny, nx) not in seen:
                    seen.add((ny, nx))
                    q.append((ny, nx))

    for b in nb[1:]:
        if b not in seen:
            return True
    return False

ans = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] == '.':
            if splits_if_block(i, j):
                ans += 1

print(ans)
