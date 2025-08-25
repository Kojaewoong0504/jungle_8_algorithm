import sys

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(N)]

    # 전처리: 행합, 열합
    rowSum = [sum(d[i]) for i in range(N)]
    colSum = [sum(d[i][j] for i in range(N)) for j in range(M)]

    INF_NEG = -10**18
    ans = INF_NEG

    # 두 행 r1<r2 고정
    for r1 in range(N):
        for r2 in range(r1 + 1, N):
            F = (r2 - r1 - 1)  # 내부행 개수 (열 간 거리와 곱해짐)

            # A[c] = colSum[c] - d[r1][c] - d[r2][c] - F*c
            # B[c] = colSum[c] - d[r1][c] - d[r2][c] + F*c
            A = [colSum[c] - d[r1][c] - d[r2][c] - F * c for c in range(M)]
            B = [colSum[c] - d[r1][c] - d[r2][c] + F * c for c in range(M)]

            base = rowSum[r1] + rowSum[r2] - F  # 식의 상수항

            bestA = A[0]
            # c1 < c2가 되어야 하므로 c2는 1부터
            for c2 in range(1, M):
                # c1은 [0..c2-1]에서 bestA로 대표
                cand = base + bestA + B[c2]
                # 교차 4칸 보정은 A,B에서 이미 빠짐
                if cand > ans:
                    ans = cand
                if A[c2] > bestA:
                    bestA = A[c2]

    print(ans)

if __name__ == "__main__":
    solve()
