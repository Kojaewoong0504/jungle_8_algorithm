import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

# 위치들 추출
start = None
home = None
fish_list = []

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'H':
            home = (i, j)
        elif grid[i][j] == 'F':
            fish_list.append((i, j))


# BFS 함수: 시작점에서 모든 위치까지 최단 거리 맵 반환
def bfs(sr, sc):
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    q.append((sr, sc))
    dist[sr][sc] = 0

    while q:
        r, c = q.popleft()
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if grid[nr][nc] != 'D' and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    return dist


dist_from_start = bfs(*start)
dist_from_home = bfs(*home)

# 최소 거리 초기화
min_total = float('inf')
for fr, fc in fish_list:
    to_fish = dist_from_start[fr][fc]
    to_home = dist_from_home[fr][fc]
    if to_fish != -1 and to_home != -1:
        min_total = min(min_total, to_fish + to_home)

print(min_total if min_total != float('inf') else -1)
