from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
draw = [list(map(str, input()[:])) for _ in range(n)]

def bfs(visited):
    while q:
        x, y, color = q.popleft()

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and draw[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx, ny, color))

normal_count = 0

q = deque()
normal_visited = [[False for _ in range(n)] for _ in range(n)]

# 정상인
for i in range(n):
    for j in range(n):
        if not normal_visited[i][j]:
            normal_visited[i][j] = True
            q.append((i, j, draw[i][j]))
            bfs(normal_visited)
            normal_count += 1

normal_visited = [[False for _ in range(n)] for _ in range(n)]
# 적록색약
for i in range(n):
    for j in range(n):
        if draw[i][j] == "G":
            draw[i][j] = "R"

rg_count = 0

for i in range(n):
    for j in range(n):
        if not normal_visited[i][j]:
            normal_visited[i][j] = True
            q.append((i, j, draw[i][j]))
            bfs(normal_visited)
            rg_count += 1

print(f"{normal_count} {rg_count}")