import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
parent = [i for i in range(n+1)]

def get_dist(loc1, loc2):
    x1, y1, x2, y2 = loc1[0], loc1[1], loc2[0], loc2[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges = [0] * (n+1)
for i in range(1, n+1):
    edges[i] = list(map(int, input().split()))

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

possible = []
for i in range(1, len(edges)-1):
    for j in range(i+1, len(edges)):
        possible.append([get_dist(edges[i], edges[j]), i, j])

possible.sort()
ans = 0

for p in possible:
    cost, x, y = p[0], p[1], p[2]

    if get_parent(x) != get_parent(y):
        union(x, y)
        ans += cost
print("{:.2f}".format(ans))