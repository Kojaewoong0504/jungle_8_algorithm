from collections import deque

n = int(input())

danji = [[int(i) for i in input()[:]] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

def bfs(num):
    while q:
        x, y = q.popleft()

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and danji[nx][ny] != 0:
                    visited[nx][ny] = True
                    danji[nx][ny] = num
                    q.append((nx,ny))


q = deque()
num = 1

for i in range(n):
    for j in range(n):
        if danji[i][j] == 1:
            if not visited[i][j]:
                visited[i][j] = True
                q.append((i,j))
                danji[i][j] = num
                bfs(num)
                num += 1

result = [0 for _ in range(num)]

print(num-1)
for i in range(n):
    for j in range(n):
        if danji[i][j] != 0:
            result[danji[i][j]] += 1
result.sort()
for i in range(1, num):
    print(result[i])