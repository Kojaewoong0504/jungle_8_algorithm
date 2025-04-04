import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x,y):
    x, y = find(x), find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m, t = map(int, input().split())

edges = []
parent = [i for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append([a,b,c])
edges.sort(key=lambda x:x[2])

cost = 0

for edge in edges:
    u, v, c = edge
    if find(u) != find(v):
        union(u,v)
        cost += c
        for i in edges:
            i[2] = i[2] + t

print(cost)