from collections import deque

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1,  0,  1, -1, 1, -1, 0, 1]

q = deque()

for i in range(n):
    for j in range(m):
        if area[i][j] == 1:
            q.append((i, j))
            dist[i][j] = 0

while q:
    x, y = q.popleft()
    for dir in range(8):
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

answer = max(max(row) for row in dist)
print(answer)
