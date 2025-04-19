import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]

q = deque()

def bfs():
    while q:
        z,x,y = q.popleft()

        dx = [-1,1,0,0,0,0]
        dy = [0,0,-1,1,0,0]
        dz = [0,0,0,0,-1,1]

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if not visited[nz][nx][ny] and box[nz][nx][ny] == 0:
                    visited[nz][nx][ny] = True
                    box[nz][nx][ny] = box[z][x][y] + 1
                    q.append((nz,nx,ny))

for z in range(h):
    for x in range(n):
        for y in range(m):
            if box[z][x][y] == 1:
                q.append((z,x,y))
                visited[z][x][y] = True

bfs()

max_count = 1

for z in range(h):
    for x in range(n):
        for y in range(m):
            if box[z][x][y] == 0:
                print("-1")
                exit()
            if box[z][x][y] > max_count:
                max_count = box[z][x][y]
print(max_count-1)