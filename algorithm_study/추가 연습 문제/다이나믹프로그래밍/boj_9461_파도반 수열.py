t = int(input())

for _ in range(t):
    num = int(input())
    dp = [0] * 101
    for n in range(1, num+1):
        if n == 1:
            dp[1] = 1
        elif n == 2:
            dp[2] = 1
        elif n == 3:
            dp[3] = 1
        else:
            dp[n] = dp[n-3] + dp[n-2]
    print(dp[num])