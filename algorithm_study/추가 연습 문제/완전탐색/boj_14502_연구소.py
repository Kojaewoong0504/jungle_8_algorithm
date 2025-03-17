from itertools import combinations
from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

area = [list(map(int, input().split())) for _ in range(n)]
blank = []
blank_comb = []

for i in range(n):
    for j in range(m):
        if area[i][j] == 0:
            blank.append((i, j))

blank_comb = list(combinations(blank, 3))
max_safe_area = -float('INF')


def bfs(copy_area):
    while q:
        x, y = q.popleft()
        visited[x][y] = 1

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if copy_area[nx][ny] != 1 and visited[nx][ny] == 0:
                    copy_area[nx][ny] = 2
                    q.append((nx, ny))


for i in range(len(blank_comb)):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    copy_area = deepcopy(area)

    q = deque()
    for j in range(n):
        for k in range(m):
            if area[j][k] == 2:
                q.append((j, k))

    for wall in blank_comb[i]:
        x, y = wall
        copy_area[x][y] = 1

    bfs(copy_area)
    safe_area = 0

    for j in range(n):
        for k in range(m):
            if visited[j][k] == 0 and copy_area[j][k] == 0:
                safe_area += 1
    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)
