def sugar_delivery_dp(n):
    INF = 10 ** 9
    dp = [INF] * (n + 1)

    dp[0] = 0  # 0kg를 만들기 위해 필요한 봉지 수는 0개

    for i in range(1, n + 1):
        if i >= 3 and dp[i - 3] != INF:
            dp[i] = min(dp[i], dp[i - 3] + 1)
        if i >= 5 and dp[i - 5] != INF:
            dp[i] = min(dp[i], dp[i - 5] + 1)

    return dp[n] if dp[n] != INF else -1


def solve():
    n = int(input())
    print(sugar_delivery_dp(n))


solve()
