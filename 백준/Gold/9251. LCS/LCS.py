A = input().rstrip()
B = input().rstrip()

# DP 테이블 초기화 (크기: (len(A)+1) x (len(B)+1))
dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

# 점화식을 이용해 DP 테이블 채우기
for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i-1] == B[j-1]:              # 문자가 일치하는 경우
            dp[i][j] = dp[i-1][j-1] + 1   # 대각선 위 값 + 1
        else:                             # 문자가 일치하지 않는 경우
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # 위쪽 vs 왼쪽 중 큰 값

# 두 문자열 전체 길이 부분의 DP 값 출력 (LCS의 길이)
print(dp[len(A)][len(B)])  # 출력: 4
