from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

grounds = [list(input()) for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]

def bfs(color):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    cnt = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[ny][nx] and grounds[ny][nx] == color:
                    cnt += 1
                    visited[ny][nx] = True
                    q.append((ny,nx))
    if cnt == 0:
        return 1
    else:
        return cnt

q = deque()
cnt = 0
result = [0,0]
for i in range(m):
    for j in range(n):
        if grounds[i][j] == "W":
            if not visited[i][j]:
                q.append((i,j))
                val_w = bfs("W")
                result[0] += (val_w**2)
        elif grounds[i][j] == "B":
            if not visited[i][j]:
                q.append((i,j))
                val_b = bfs("B")
                result[1] += (val_b**2)

print(*result)
