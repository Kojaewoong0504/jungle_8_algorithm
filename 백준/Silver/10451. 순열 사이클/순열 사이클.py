import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    perm = [0] + list(map(int, input().split()))
    visited = [False] * (N + 1)

    cycle_count = 0

    for i in range(1, N + 1):
        if not visited[i]:
            cycle_count += 1
            cur = i
            while not visited[cur]:
                visited[cur] = True
                cur = perm[cur]

    print(cycle_count)