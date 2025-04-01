from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

farm = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]


def bfs():
    global trigger
    dx = [-1,1,0,0,1,-1,1,-1]
    dy = [0,0,-1,1,-1,-1,1,1]
    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if farm[x][y] < farm[nx][ny]:
                    trigger = False
                if not visited[nx][ny] and farm[nx][ny] == farm[x][y]:
                    visited[nx][ny] = True
                    q.append((nx,ny))



q = deque()
cnt = 0
for i in range(n):
    for j in range(m):
        if farm[i][j] > 0 and not visited[i][j]:
            visited[i][j] = True
            trigger = True
            q.append((i,j))
            bfs()

            if trigger:
                cnt+=1
print(cnt)