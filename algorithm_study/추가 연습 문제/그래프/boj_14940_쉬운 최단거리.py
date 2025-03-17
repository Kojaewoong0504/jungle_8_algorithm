from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())


area = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
result = [[0 for _ in range(m)] for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if area[i][j] == 1:
            result[i][j] = -1
        if area[i][j] == 2:
            q.append((i,j))
            visited[i][j] = True

while q:
    x, y = q.popleft()

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if area[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                result[nx][ny] = result[x][y] + 1
                q.append((nx,ny))

for i in range(n):
    for j in range(m):
        print(result[i][j], end= " ")
    print("")


