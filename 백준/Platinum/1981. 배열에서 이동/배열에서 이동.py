from collections import deque

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(a,b):
    if not (a <= board[0][0] <= b):
        return False
    q = deque()
    q.append((0,0))
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        if (x, y) == (n-1, n-1):
            return True
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and a <= board[nx][ny] <= b:
                    visited[nx][ny] = True
                    q.append((nx,ny))



left, right = 0, 200
ans = 200
while left <= right:
    mid = (left + right) // 2
    possible = False

    for a in range(201-mid):
        if bfs(a, a+mid):
            possible = True
            break

    if possible:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)