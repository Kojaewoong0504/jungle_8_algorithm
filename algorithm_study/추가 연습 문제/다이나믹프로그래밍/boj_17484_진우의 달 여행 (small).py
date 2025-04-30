n, m = map(int, input().split())

space = [list(map(int, input().split())) for _ in range(n)]

INF = int(1e9)
dp = [[[INF]*3 for _ in range(m)] for _ in range(n)]

for j in range(m):
    for dir in range(3):
        dp[0][j][dir] = space[0][j]

dy = [1, 1, 1]
dx = [-1, 0, 1]

for i in range(1, n):
    for j in range(m):
        for dir in range(3): # 현재 방향
            prev_j = j + dx[dir]
            if 0 <= prev_j < m:
                for prev_dir in range(3): # 이전 방향
                    if prev_dir != dir: # 같은 방향으로 두 번 못 움직임
                        dp[i][j][dir] = min(dp[i][j][dir], dp[i-1][prev_j][prev_dir] + space[i][j])

# 마지막 줄에서 최소값
ans = INF
for j in range(m):
    for dir in range(3):
        ans = min(ans, dp[n-1][j][dir])

print(ans)