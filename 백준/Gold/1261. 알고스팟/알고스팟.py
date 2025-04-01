from collections import deque

m, n = map(int, input().split())

maze = []
graph = [[-1] * m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(n):
    maze.append(list(map(int, list(input()))))

q = deque([[0, 0]])
graph[0][0] = 0
while q:
    x, y = q.popleft()
    for idx in range(4):
        
        nx = x + dx[idx]
        ny = y + dy[idx]
        
        if (nx == n - 1) & (ny == m - 1):
            graph[nx][ny] = graph[x][y]
            q.clear()
            break
        if (0 <= nx < n) & (0 <= ny < m):
            if graph[nx][ny] == -1:
                if maze[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx, ny])
                elif maze[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y]
                    q.appendleft([nx, ny])

print(graph[n - 1][m - 1])