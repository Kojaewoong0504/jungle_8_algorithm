import sys
input = sys.stdin.readline

n = int(input())
nums = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
cases = int(input())


for i in range(n, 0, -1):
    for j in range(i, n + 1):
        if nums[i] == nums[j]:
            if j - i <= 1:
                dp[i][j] = 1
            elif dp[i + 1][j - 1] == 1:
                dp[i][j] = 1

for _ in range(cases):
    start, end = map(int, input().split())
    print(dp[start][end])
