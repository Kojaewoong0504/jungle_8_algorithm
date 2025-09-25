import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    S = input().strip()
    h0 = S.count('H')  # 초기 앞면 개수

    # 빠른 컷
    if h0 == 0:
        print(0)
        return
    if K == N:
        print(1 if h0 == N else -1)
        return
    if K % 2 == 0 and (h0 % 2 == 1):
        print(-1)
        return

    dist = [-1] * (N + 1)
    dist[h0] = 0
    q = deque([h0])

    while q:
        h = q.popleft()

        x_min = max(0, K - (N - h))
        x_max = min(h, K)
        for x in range(x_min, x_max + 1):
            h2 = h + K - 2 * x
            if 0 <= h2 <= N and dist[h2] == -1:
                dist[h2] = dist[h] + 1
                if h2 == 0:
                    print(dist[h2])
                    return
                q.append(h2)

    print(-1)

if __name__ == "__main__":
    solve()