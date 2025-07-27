from collections import deque


def bfs(x, y):
    res = 0
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        res += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n and 0 <= ny < m):
                if (graph[nx][ny] == 1):
                    queue.append((nx, ny))
                    graph[nx][ny] = 0
    return res


n, m, k = map(int, input().split())
size = []
graph = [[0] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(k):
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = 1

for i in range(n):
    for j in range(m):
        if (graph[i][j] == 1):
            size.append(bfs(i, j))

print(max(size))
