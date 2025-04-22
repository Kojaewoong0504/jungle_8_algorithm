import sys
input = sys.stdin.readline

n = int(input())
nums = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
cases = int(input())

for i in range(1, n + 1):
    dp[i][i] = 1

for i in range(1, n):
    if nums[i] == nums[i + 1]:
        dp[i][i + 1] = 1

for length in range(3, n + 1):
    for start in range(1, n - length + 2):
        end = start + length - 1
        if nums[start] == nums[end] and dp[start + 1][end - 1] == 1:
            dp[start][end] = 1


for _ in range(cases):
    start, end = map(int, input().split())
    print(dp[start][end])



