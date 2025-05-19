import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
s, e = map(int, input().split())


def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = 0
    while q:
        node = q.popleft()
        d = [node - 1, node + 1]
        if graph[node]:
            d += graph[node]
        for i in d:
            if (1 <= i <= n) and visited[i] == -1:
                q.append(i)
                visited[i] = visited[node] + 1
            if i == e:
                return visited[i]


graph = [[] for _ in range(n + 1)]
visited = [-1 for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
cnt = bfs(s)
print(cnt)
