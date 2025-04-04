from collections import deque

n, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
S, X, Y = map(int, input().split())

data = []
for i in range(n):
    for j in range(n):
        if maps[i][j] != 0:
            data.append((maps[i][j], i, j, 0))

data.sort(key=lambda x: x[0])

q = deque(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    virus, x, y, t = q.popleft()

    if t == S:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if maps[nx][ny] == 0:
                maps[nx][ny] = virus
                q.append((virus, nx, ny, t + 1))

answer = maps[X-1][Y-1]
if answer == 0:
    print(0)
else:
    print(answer)
