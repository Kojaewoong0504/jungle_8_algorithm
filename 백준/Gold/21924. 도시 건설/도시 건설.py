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


n, m = map(int, input().split())

edges = []
parent = [i for i in range(n+1)]

total_cost = 0

for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((a,b,c))
    total_cost += c
edges.sort(key= lambda x: x[2])

cost = 0
count_edges = 0  # MST에 실제로 포함된 간선 수

for edge in edges:
    u, v, c = edge
    if find(u) != find(v):
        union(u,v)
        cost += c
        count_edges += 1

if count_edges == n-1:
    # 모든 건물이 연결됨
    print(total_cost - cost)
else:
    # 일부 건물이 고립되어 연결되지 않았음
    print(-1)