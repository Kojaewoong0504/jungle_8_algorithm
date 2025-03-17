from collections import deque
import sys
input = sys.stdin.readline

def bfs(start_x, start_y):
    q = deque([(start_x,start_y)])
    visited[start_x][start_y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if area[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    area = [[0 for _ in range(n)] for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        point_x, point_y = map(int, input().split())
        area[point_x][point_y] = 1

    worm_count = 0

    for i in range(m):
        for j in range(n):
            if area[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                worm_count += 1
    print((worm_count))


