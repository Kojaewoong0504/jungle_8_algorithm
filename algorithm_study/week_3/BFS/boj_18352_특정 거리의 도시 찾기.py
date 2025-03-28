import sys
from collections import deque
input = sys.stdin.readline
n, m, k, start = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)

def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = 0
    while q:
        node = q.popleft()

        if visited[node] >= k:
            continue
        for i in graph[node]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[node] + 1

bfs(start)

result = []
for i in range(1, n+1):
    if visited[i] == k:
        result.append(i)

if result:
    for city in result:
        print(city)
else:
    print(-1)

