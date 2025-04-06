n = int(input())

nums = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[0][0] = nums[0][0]
if n > 1:
    dp[1][0] = nums[1][0] + dp[0][0]
    dp[1][1] = nums[1][1] + dp[0][0]

for i in range(2, n):
    for j in range(len(nums[i])):
        if j == 0:
            dp[i][j] = nums[i][j] + dp[i-1][0]
        elif j == len(nums[i]) - 1:
            dp[i][j] = nums[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = nums[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1][:n]))
