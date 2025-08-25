import sys
from collections import deque

input = sys.stdin.readline

h, w = map(int, input().split())
maps = [list(input().strip()) for _ in range(h)]

dx = [-1,1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,-1,1,-1,1]

q = deque()

start = end = None
for i in range(h):
    for j in range(w):
        if maps[i][j] == 'K':
            start = (i, j)
        elif maps[i][j] == '*':
            end = (i, j)

INF = 10**15
visited = [[INF] * w for _ in range(h)]

sx, sy = start
visited[sx][sy] = 0
q.append((sx, sy))

while q:
    x, y = q.popleft()
    if (x, y) == end:
        print(visited[x][y])
        break

    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] != "#":
            cost = 0 if ny == y + 1 else 1
            nd = visited[x][y] + cost
            if nd < visited[nx][ny]:
                visited[nx][ny] = nd
                # 0-1 BFS: 0이면 왼쪽, 1이면 오른쪽
                if cost == 0:
                    q.appendleft((nx, ny))
                else:
                    q.append((nx, ny))
else:
    print(-1)
