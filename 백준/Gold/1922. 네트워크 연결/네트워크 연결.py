n = int(input())
m = int(input())


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a,b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(n+1)]
edges = []

for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((a,b,c))
edges.sort(key = lambda x : x[2])

cost = 0

for edge in edges:
    u, v, c = edge
    if find(u) != find(v):
        union(u,v)
        cost += c
print(cost)