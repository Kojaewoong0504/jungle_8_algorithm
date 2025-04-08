import math
import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
dp[0] = 0  # 0은 0개 항 필요

for i in range(1, n + 1):
    dp[i] = i  # 최악의 경우: 1^2 + 1^2 + ... + 1^2 (i번)
    for j in range(1, math.isqrt(i) + 1):
        dp[i] = min(dp[i], dp[i - j * j] + 1)

print(dp[n])
