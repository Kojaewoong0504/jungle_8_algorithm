import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

m, n = map(int, input().split())
n, m = m, n

maps = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]


def dfs(data):
    x, y = data
    if x == n-1 and y == m-1:
        return 1

    if dp[x][y] == -1:

        dp[x][y] = 0

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] < maps[x][y]:
                    dp[x][y] += dfs((nx,ny))
    return dp[x][y]

print(dfs((0, 0)))