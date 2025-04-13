n = int(input())

dp = [-1] * (n+1)

if n >= 2:
    dp[2] = 1

if n >= 4:
    dp[4] = 2
if n >= 5:
    dp[5] = 1

for i in range(6, n+1):
    if dp[i-2] != -1 and dp[i-5] != -1:
        dp[i] = min(dp[i-2]+1, dp[i-5]+1)
    elif dp[i-2] != -1:
        dp[i] = dp[i-2] + 1
    elif dp[i-5] != -1:
        dp[i] = dp[i-5] + 1

print(dp[n])


# n = int(input())
#
# count = 0
# while n >= 0:
#     if n % 5 == 0:
#         count += n // 5
#         print(count)
#         break
#     n -= 2
#     count += 1
# else:
#     print(-1)