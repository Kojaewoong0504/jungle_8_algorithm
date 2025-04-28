import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(input().strip()) for _ in range(n)]
visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0, 0, 0, 1))  # (x, y, broken, distance)
visited[0][0][0] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    x, y, broken, dist = q.popleft()

    if x == m - 1 and y == n - 1:
        print(dist)
        exit(0)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if graph[ny][nx] == "1" and broken == 0 and not visited[ny][nx][1]:
                visited[ny][nx][1] = True
                q.append((nx, ny, 1, dist + 1))
            elif graph[ny][nx] == "0" and not visited[ny][nx][broken]:
                visited[ny][nx][broken] = True
                q.append((nx, ny, broken, dist + 1))

print(-1)
