n = int(input())


INF = 10 ** 8
dp = [INF] * (n+1)

for i in range(n+1):
    if i == 0 or i == 1:
        dp[i] = 0
        continue
    if i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[i-1] + 1, dp[i//3] + 1, dp[i//2] + 1)
    elif i % 3 == 0 and i % 2 != 0:
        dp[i] = min(dp[i-1] + 1, dp[i//3] + 1)
    elif i % 2 == 0 and i % 3 != 0:
        dp[i] = min(dp[i-1] + 1, dp[i//2] + 1)
    else:
        dp[i] = dp[i-1] + 1

print(dp[n])