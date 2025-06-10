from collections import deque

n, m = map(int, input().split())
inside, outside = map(int, input().split())
maps = [list(input().strip()) for _ in range(n)]

visited = [[[False] * 101 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'S':
            sx, sy = i, j
        elif maps[i][j] == 'E':
            ex, ey = i, j


def is_indoor(x, y):
    return maps[x][y] in ('H', 'S')


q = deque()
q.append((sx, sy, 0, 0))
visited[sx][sy][0] = True

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while q:
    x, y, b, t = q.popleft()

    if (x, y) == (ex, ey):
        print(t)
        exit(0)

    for dx, dy in dirs + [(0, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if maps[nx][ny] == "#":
                continue
            nb = b
            if is_indoor(nx, ny):
                nb = max(0, nb - inside)
            else:
                nb = min(100, nb + outside)

            if nb >= 100:
                continue

            if not visited[nx][ny][nb]:
                visited[nx][ny][nb] = True
                q.append((nx, ny, nb, t + 1))
print(-1)
