import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

def dfs(node):
    visited[node] = True
    for child in graph[node]:
        if not visited[child]:
            parents[child] = node
            dfs(child)

parents = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for i in range(2, n+1):
    print(parents[i])