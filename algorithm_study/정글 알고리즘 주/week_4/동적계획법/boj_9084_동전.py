import sys
input = sys.stdin.readline

t = int(input())


for i in range(t):
    n = int(input().strip())
    coins = list(map(int, input().split()))
    k = int(input().strip())

    dp = [0]*(k+1)
    dp[0] = 1

    for j in range(len(coins)):
        c = coins[j]
        for k in range(c, k+1):
            dp[k] += dp[k-c]

    print(dp[k])