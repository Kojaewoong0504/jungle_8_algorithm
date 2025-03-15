from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
area = []
max_height = 0


for i in range(n):
    area.append(list(map(int, input().split())))
    for j in range(n):
        if area[i][j] > max_height:
            max_height = area[i][j]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(a, b, water_height, visited):
    q = deque()
    q.append((a, b))
    visited[a][b] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if area[nx][ny] > water_height and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])

result = 0
for i in range(max_height):
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if area[j][k] > i and visited[j][k] == 0:
                bfs(j,k, i, visited)
                cnt += 1
    if result < cnt:
        result = cnt

print(result)

