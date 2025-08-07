from collections import deque

board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

visited = [[-1 for _ in range(5)] for _ in range(5)]

q = deque()
q.append((r, c))
visited[r][c] = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

target = []
for i in range(5):
    for j in range(5):
        if board[i][j] == 1:
            target.append((i, j))


while q:
    cur_r, cur_c = q.popleft()
    for i in range(4):
        nr, nc = cur_r + dx[i], cur_c + dy[i]
        if 0 <= nr < 5 and 0 <= nc < 5:
            if not board[nr][nc] == -1 and visited[nr][nc] == -1:
                visited[nr][nc] = visited[cur_r][cur_c] + 1
                q.append((nr, nc))

target_x, target_y = target[0]
print(visited[target_x][target_y])