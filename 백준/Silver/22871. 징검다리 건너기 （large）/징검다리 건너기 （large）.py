n = int(input())
A = list(map(int, input().split()))

INF = 10**20
dp = [INF] * n
dp[0] = 0

for j in range(1, n):
    Aj = A[j]
    best = INF
    for i in range(j):
        c = (j - i) * (1 + abs(A[i] - Aj))
        cand = dp[i] if dp[i] > c else c
        if cand < best:
            best = cand
    dp[j] = best

print(dp[-1])