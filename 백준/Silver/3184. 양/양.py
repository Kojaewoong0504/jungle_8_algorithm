from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, b):
    sheep = 0
    wolf = 0

    q = deque()
    q.append((a, b))

    if graph[a][b] == 'o':
        sheep += 1
    elif graph[a][b] == 'v':
        wolf += 1

    graph[a][b] = '#'

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != "#":
                if graph[nx][ny] == 'o':
                    sheep += 1
                elif graph[nx][ny] == 'v':
                    wolf += 1

                graph[nx][ny] = '#'
                q.append((nx, ny))

    if wolf >= sheep:
        return 0, wolf
    elif sheep > wolf:
        return sheep, 0


r, c = map(int, input().split())
graph = []

total_sheep = 0
total_wolf = 0

for i in range(r):
    graph.append(list(input()))

for i in range(r):
    for j in range(c):
        if graph[i][j] in 'ov':
            tempSheep, tempWolf = bfs(i, j)
            total_sheep += tempSheep
            total_wolf += tempWolf

print(total_sheep, total_wolf)