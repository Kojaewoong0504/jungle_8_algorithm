from collections import deque
import sys

input = sys.stdin.readline

h, w = map(int, input().split())
visited = [[False for _ in range(w)] for _ in range(h)]
prison = [["." for _ in range(w+2)]]
for y in range(h):
    row = list(input()[:-1])
    prison.append(["."] + row + ["."])
prison.append(["." for _ in range(w+2)])

def bfs():
    while q:
        x,y = q.popleft()

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and prison[nx][ny] != "*":
                    if prison[nx][ny] == "#":
                        prison[nx][ny] = prison[x][y] + 1
                    else:
                        prison[nx][ny] = prison[x][y]


q = deque()

for i in range(h):
    for j in range(w):
        if prison[i][j] == "$":
            prison[i][j] = "0"
            q.append((i,j))
            visited[i][j] = True

bfs()
print(prison)