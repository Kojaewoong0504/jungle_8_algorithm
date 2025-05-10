from collections import deque
from itertools import combinations

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

can_virus = [(i, j) for i in range(n) for j in range(n) if lab[i][j] == 2]

min_time = float('inf')
for comb in combinations(can_virus, m):
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    q = deque()
    for y, x in comb:
        visited[y][x] = 0
        q.append((y, x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if lab[ny][nx] != 1 and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))

    valid = True
    current_time = 0
    for i in range(n):
        for j in range(n):
            if lab[i][j] != 1:
                if visited[i][j] == -1:
                    valid = False
                    break
                current_time = max(current_time, visited[i][j])
        if not valid:
            break

    if valid:
        min_time = min(min_time, current_time)

print(min_time if min_time != float('inf') else -1)