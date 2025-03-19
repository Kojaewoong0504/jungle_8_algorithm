import math
import sys
input = sys.stdin.readline

n = int(input())
dp = [0,1]

for i in range(2, n+1):
    min_count = 4
    for j in range(int(math.sqrt(i)), 0, -1):
        min_count = min(min_count, dp[i-j**2]+1)
    dp.append(min_count)

print(dp[n])