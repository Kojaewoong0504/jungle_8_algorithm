import sys
input = sys.stdin.readline

def comb2(x: int) -> int:
    return x * (x - 1) // 2

T = int(input().strip())
for _ in range(T):
    N, M, k, D = map(int, input().split())
    total_teams = N * M
    within_pairs = N * comb2(M)
    all_pairs = comb2(total_teams)
    C = all_pairs + (k - 1) * within_pairs

    if C == 0:
        print(-1)
        continue

    Bmax = D // C
    if Bmax >= 1:
        print(Bmax * C)
    else:
        print(-1)
