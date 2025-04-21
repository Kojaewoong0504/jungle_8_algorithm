import sys


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    parent[y] = x


n, q = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    arr.append((a, b, c, i))
arr.sort()

parent = [i for i in range(n)]

now_start, now_end, _, now_idx = arr[0]
for i in range(1, n):
    next_start, next_end, _, next_idx = arr[i]

    if now_start <= next_start <= now_end:
        union(now_idx, next_idx)

        if next_end >= now_end:
            now_start, now_end, now_idx = next_start, next_end, next_idx

    else:
        now_start, now_end, now_idx = next_start, next_end, next_idx

for _ in range(q):
    a, b = map(int, sys.stdin.readline().split())
    if parent[a - 1] == parent[b - 1]:
        print(1)
    else:
        print(0)