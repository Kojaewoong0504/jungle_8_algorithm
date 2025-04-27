N = int(input())

MOD = 1000000000

# dp[pos][num][bitmask] 형태로 3차원 배열 만들기
dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N + 1)]

# 초기화: 길이 1일 때 1~9로 시작하는 경우만 가능
for i in range(1, 10):
    dp[1][i][1 << i] = 1

# DP 채우기
for pos in range(1, N):
    for num in range(10):
        for bitmask in range(1 << 10):
            if dp[pos][num][bitmask] == 0:
                continue  # 값이 없으면 스킵

            # 다음 자리수로 num-1 이동
            if num > 0:
                next_num = num - 1
                next_bitmask = bitmask | (1 << next_num)
                dp[pos + 1][next_num][next_bitmask] = (dp[pos + 1][next_num][next_bitmask] + dp[pos][num][bitmask]) % MOD

            # 다음 자리수로 num+1 이동
            if num < 9:
                next_num = num + 1
                next_bitmask = bitmask | (1 << next_num)
                dp[pos + 1][next_num][next_bitmask] = (dp[pos + 1][next_num][next_bitmask] + dp[pos][num][bitmask]) % MOD

# 최종 답: 길이가 N이고, 0~9 숫자를 모두 사용한 경우 (bitmask == 1023)
ans = 0
for i in range(10):
    ans = (ans + dp[N][i][(1 << 10) - 1]) % MOD

print(ans)
