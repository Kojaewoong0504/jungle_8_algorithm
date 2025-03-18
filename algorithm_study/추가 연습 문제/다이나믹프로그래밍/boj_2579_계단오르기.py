import sys
input = sys.stdin.readline
n = int(input())

stair = []
dp = [0] * 301

for _ in range(n):
    stair.append(int(input()))

if n >= 1:
    dp[0] = stair[0]
if n >= 2:
    dp[1] = stair[0] + stair[1]
if n >= 3:
    dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

if n > 3:
    for i in range(3, n):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

print(dp[n-1])
