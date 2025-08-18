import sys
input = sys.stdin.readline

N = int(input().strip())
p1, p2 = map(int, input().split())
M = int(input().strip())
S = int(input().strip())

if p1 > p2:
    p1, p2 = p2, p1  # 안전

INF = 10**18
best = INF

# ----- 왼쪽 반죽(p1)이 고기를 붙이는 경우 -----
# 붙는 필요충분조건: |p1 - M|이 홀수
if abs(p1 - M) % 2 == 1:
    left_cost = INF

    # R이 M의 왼쪽(= p2 < M)이라면, L이 M에 서려면 R이 반드시 M을 '먼저' 지나서 >= M+1이어야 함
    # 이때 (M - p2)가 홀수면 R이 지나갈 때 고기를 먼저 붙여버리므로 불가능
    if p2 < M and (M - p2) % 2 == 1:
        left_cost = INF
    else:
        if p2 <= M:
            if M < N:
                clearToM = (M + 1) - p2
                R = M + 1
                if S < N:
                    clearToS = max(0, (S + 1) - R)
                    left_cost = abs(p1 - M) + abs(S - M) + clearToM + clearToS
                else:
                    left_cost = INF  # S == N 불가 (R >= S+1 필요)
            else:
                left_cost = INF  # M == N이면 R을 M+1로 못 민다
        else:
            # p2 > M (이미 오른쪽)
            clearToM = 0
            R = p2
            if S < N:
                clearToS = max(0, (S + 1) - R)
                left_cost = abs(p1 - M) + abs(S - M) + clearToM + clearToS
            else:
                left_cost = INF

    best = min(best, left_cost)

# ----- 오른쪽 반죽(p2)이 고기를 붙이는 경우 -----
# 붙는 필요충분조건: |p2 - M|이 홀수
if abs(p2 - M) % 2 == 1:
    right_cost = INF

    # L이 M의 오른쪽(= p1 > M)이라면, R이 M에 서려면 L이 반드시 M을 '먼저' 지나서 <= M-1이어야 함
    # 이때 (p1 - M)이 홀수면 L이 지나갈 때 고기를 먼저 붙여버리므로 불가능
    if p1 > M and (p1 - M) % 2 == 1:
        right_cost = INF
    else:
        if p1 >= M:
            if M > 1:
                clearToM = p1 - (M - 1)
                L = M - 1
                if S > 1:
                    clearToS = max(0, L - (S - 1))
                    right_cost = abs(p2 - M) + abs(S - M) + clearToM + clearToS
                else:
                    right_cost = INF  # S == 1 불가 (L <= S-1 필요)
            else:
                right_cost = INF  # M == 1이면 L을 M-1로 못 민다
        else:
            # p1 < M (이미 왼쪽)
            clearToM = 0
            L = p1
            if S > 1:
                clearToS = max(0, L - (S - 1))
                right_cost = abs(p2 - M) + abs(S - M) + clearToM + clearToS
            else:
                right_cost = INF

    best = min(best, right_cost)

print(-1 if best == INF else best)
