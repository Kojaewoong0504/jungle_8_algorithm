from itertools import combinations
from collections import deque

N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]

houses = []
spaces = []

for r in range(N):
    for c in range(M):
        if grid[r][c] == '1':
            houses.append((r, c))
        else:
            spaces.append((r, c))

# 방향 벡터 (상, 하, 좌, 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(start1, start2):
    visited = [[-1] * M for _ in range(N)]
    q = deque()

    # 독주머니 두 곳
    q.append((start1[0], start1[1], 0))
    q.append((start2[0], start2[1], 0))
    visited[start1[0]][start1[1]] = 0
    visited[start2[0]][start2[1]] = 0

    while q:
        r, c, time = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == -1:
                visited[nr][nc] = time + 1
                q.append((nr, nc, time + 1))

    max_time = 0
    for hr, hc in houses:
        if visited[hr][hc] == -1:
            return float('inf')  # 이 조합으로는 모든 마을 감염 불가
        max_time = max(max_time, visited[hr][hc])
    return max_time

ans = float('inf')
for p1, p2 in combinations(spaces, 2):
    cost = bfs(p1, p2)
    ans = min(ans, cost)

print(ans)
