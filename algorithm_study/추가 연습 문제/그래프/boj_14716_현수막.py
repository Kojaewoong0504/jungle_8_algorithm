from collections import deque
import sys

input = sys.stdin.readline
m, n = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]

dx = [-1, 1, -1, 1, 0, 0, -1, 1]
dy = [-1, 1, 1, -1, 1, -1, 0, 0]

q = deque()

def bfs():
    while q:
        y, x = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[ny][nx] and board[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((ny,nx))

cnt = 0
for i in range(m):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            q.append((i,j))
            bfs()
            cnt += 1

print(cnt)