def solution(mats, park):
    # 행마다 길이가 다를 수 있어도 안전하게 처리
    h = len(park)
    W = max(len(row) for row in park) if h else 0

    # DP[i][j] = (i,j)를 우하단으로 하는 "빈 칸만으로 이루어진" 최대 정사각형 변 길이
    dp = [[0] * W for _ in range(h)]
    max_square = 0

    for i in range(h):
        row_len = len(park[i])
        for j in range(row_len):
            if park[i][j] == "-1":
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    # 위/왼/왼위 값이 존재하는 경우만 사용 (행 길이가 서로 다를 수 있으므로 가드)
                    up     = dp[i-1][j]   if j < len(park[i-1]) else 0
                    left   = dp[i][j-1]   if j-1 >= 0 else 0
                    upleft = dp[i-1][j-1] if (j-1 >= 0 and j-1 < len(park[i-1])) else 0
                    dp[i][j] = 1 + min(up, left, upleft)
                if dp[i][j] > max_square:
                    max_square = dp[i][j]
            # 사람이 앉아 있으면 dp[i][j] = 0 (초기값 그대로)

    # 가장 큰 빈 정사각형 변 길이 이하인 돗자리 중 최댓값
    candidates = [s for s in mats if s <= max_square]
    return max(candidates) if candidates else -1