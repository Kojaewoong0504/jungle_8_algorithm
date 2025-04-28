import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[False for _ in range(m)] for _ in range(n)]
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_sum = -float('INF')


def check_T_shape(x, y):
    global max_sum
    t_shapes = [
        [(0, 0), (0, -1), (0, 1), (-1, 0)],  # 위쪽으로 뻗은 T
        [(0, 0), (0, -1), (0, 1), (1, 0)],  # 아래쪽으로 뻗은 T
        [(0, 0), (-1, 0), (1, 0), (0, -1)],  # 왼쪽으로 뻗은 T
        [(0, 0), (-1, 0), (1, 0), (0, 1)],  # 오른쪽으로 뻗은 T
    ]
    for shape in t_shapes:
        try:
            total = 0
            for dx, dy in shape:
                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    raise IndexError
                total += board[nx][ny]
            max_sum = max(max_sum, total)
        except IndexError:
            continue  # 범위 넘어가면 그냥 넘김


def dfs(x, y, depth, total):
    global max_sum
    if depth == 4:
        max_sum = max(max_sum, total)
        return

    for dir in range(4):  # 4방향 이동
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, depth + 1, total + board[nx][ny])
                visited[nx][ny] = False  # 복구


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        check_T_shape(i, j)  # T자 모양은 따로 체크

print(max_sum)