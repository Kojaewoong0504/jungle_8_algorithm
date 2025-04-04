import sys
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

parent = [i for i in range(n+1)]


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

edges = []

for i in range(n):
    for j in range(n):
        if not i == j:
            edges.append((i,j,graph[i][j]))

edges.sort(key=lambda x:x[2])

cost = 0
for edge in edges:
    u, v, c = edge
    if find(u) != find(v):
        union(u,v)
        cost += c

print(cost)