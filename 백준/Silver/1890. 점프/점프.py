import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        val = int(board[i][j])
        if val == 0 or dp[i][j] == 0:
            continue
        if i + val < n:
            dp[i + val][j] += dp[i][j]
        if j + val < n:
            dp[i][j+val] += dp[i][j]
print(dp[-1][-1])