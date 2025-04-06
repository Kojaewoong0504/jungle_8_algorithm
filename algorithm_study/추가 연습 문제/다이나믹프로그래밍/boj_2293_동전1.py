import sys
input = sys.stdin.readline


n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

dp = [0]*(k+1)
dp[0] = 1

for j in range(len(coins)):
    c = coins[j]
    for k in range(c, k+1):
        dp[k] += dp[k-c]

print(dp[k])