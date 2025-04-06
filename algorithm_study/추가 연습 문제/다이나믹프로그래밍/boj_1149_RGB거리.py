import sys

input = sys.stdin.readline

N = int(input().strip())
costs = [list(map(int, input().split())) for _ in range(N)]

# dp[i][c] = i번 집까지 칠했을 때,
#           i번 집의 색을 c로 고정했을 때의 최소 비용
dp = [[0]*3 for _ in range(N)]

# 첫 번째 집 초기화
dp[0][0] = costs[0][0]
dp[0][1] = costs[0][1]
dp[0][2] = costs[0][2]

# 점화식 적용
for i in range(1, N):
    dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])

# N번째 집을 빨강, 초록, 파랑 중 어떤 색으로 칠하더라도
# 그 중 최솟값이 최종 답
print(min(dp[N-1]))
