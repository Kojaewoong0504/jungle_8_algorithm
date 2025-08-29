N, M = map(int, input().split())
cuts = list(map(int, input().split()))

cuts = [0] + sorted(cuts) + [N]
L = len(cuts)  # = M + 2

dp = [[0] * L for _ in range(L)]
opt = [[0] * L for _ in range(L)]  # 최적 분할점 저장

# 초기화: 인접한 구간은 잘라야 할 게 없음
for i in range(L - 1):
    opt[i][i + 1] = i + 1

# 구간 길이를 2 이상부터 늘려가며 계산
for length in range(2, L):
    for i in range(L - length):
        j = i + length
        dp[i][j] = float('inf')

        # 탐색 범위를 opt[i][j-1] ~ opt[i+1][j]로 제한
        left, right = opt[i][j - 1], opt[i + 1][j]
        for k in range(left, right + 1):
            cost = dp[i][k] + dp[k][j] + (cuts[j] - cuts[i])
            if cost < dp[i][j]:
                dp[i][j] = cost
                opt[i][j] = k

print(dp[0][L - 1])
