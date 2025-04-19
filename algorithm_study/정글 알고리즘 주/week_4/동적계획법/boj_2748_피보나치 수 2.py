n = int(input())
dp = [0] * n

for i in range(n):
    if i == 0:
        dp[0] = 1
    elif i == 1:
        dp[1] = 1
    else:
        dp[i] = dp[i-2] + dp[i-1]

print(dp[n-1])