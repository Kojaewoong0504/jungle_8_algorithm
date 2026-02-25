import sys
sys.setrecursionlimit(200000)
n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort(reverse=True)

def dfs(node, d):
    visited[node] = True
    depth[node] = d

    for next in graph[node]:
        if not visited[next]:
            dfs(next, d + 1)

visited = [False] * (n+1)
depth = [-1] * (n+1)

dfs(r, 0)
for i in range(1, n+1):
    print(depth[i])