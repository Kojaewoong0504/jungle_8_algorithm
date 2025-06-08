import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

n = int(input())
mp, mf, ms, mv = map(int, input().split())
nutrients = [list(map(int, input().split())) for _ in range(n)]

min_cost = float('inf')
result = []


def recursion(p, f, s, v, cost, start, path):
    global min_cost, result

    if p >= mp and f >= mf and s >= ms and v >= mv:
        if cost < min_cost:
            min_cost = cost
            result = path[:]
        elif cost == min_cost:
            if path < result:
                result = path[:]

    for i in range(start, n):
        np, nf, ns, nv, next_cost = nutrients[i]
        recursion(p + np, f + nf, s + ns, v + nv, cost + next_cost, i + 1, path + [i + 1])


recursion(0, 0, 0, 0, 0, 0, [])

if result:
    print(min_cost)
    print(' '.join(map(str, result)))
else:
    print(-1)