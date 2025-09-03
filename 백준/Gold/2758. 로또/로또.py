import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for x in range(1, m + 1):
        dp[1][x] = 1

    for k in range(2, n + 1):
        prefix = [0] * (m + 1)
        for x in range(1, m + 1):
            prefix[x] = prefix[x - 1] + dp[k - 1][x]
        for x in range(1, m + 1):
            dp[k][x] = prefix[x // 2]

    print(sum(dp[n]))
