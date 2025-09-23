import sys

n = int(sys.stdin.readline().strip())

dp = [0] * n
dp[0] = 2

for i in range(1, n):
    dp[i] = dp[i - 1] * 2 + dp[i - 1]

print(dp[n - 1])