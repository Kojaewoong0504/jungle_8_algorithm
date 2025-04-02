n, m = map(int, input().split())


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
parent = [i for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a,b,c))
edges.sort(key= lambda x:x[2])

cost = 0
mst_edges = []

for edge in edges:
    u, v, c = edge
    if find(u) != find(v):
        union(u,v)
        cost += c
        mst_edges.append(c)

max_edge = max(mst_edges)
print(cost - max_edge)