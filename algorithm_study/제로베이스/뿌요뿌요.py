from collections import deque
import copy

def simulate_puyo(board):
    R, C = len(board), len(board[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y, visited):
        color = board[x][y]
        q = deque()
        q.append((x, y))
        group = [(x, y)]
        visited[x][y] = True

        while q:
            cx, cy = q.popleft()
            for d in range(4):
                nx, ny = cx + dx[d], cy + dy[d]
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                    if board[nx][ny] == color:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        group.append((nx, ny))
        return group

    def apply_gravity():
        for col in range(C):
            stack = []
            for row in range(R-1, -1, -1):
                if board[row][col] != 0:
                    stack.append(board[row][col])
            for row in range(R-1, -1, -1):
                if stack:
                    board[row][col] = stack.pop(0)
                else:
                    board[row][col] = 0

    while True:
        visited = [[False]*C for _ in range(R)]
        to_remove = set()
        for i in range(R):
            for j in range(C):
                if board[i][j] != 0 and not visited[i][j]:
                    group = bfs(i, j, visited)
                    if len(group) >= 3:
                        to_remove.update(group)

        if not to_remove:
            break  # 더 이상 터질 블록 없음

        for x, y in to_remove:
            board[x][y] = 0  # 제거

        apply_gravity()

    return board
