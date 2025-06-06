from collections import deque
import sys

input = sys.stdin.readline


def bfs(s):
    global result
    q = deque()
    q.append((s, 0))

    while q:
        v, dist = q.popleft()

        visited[v] = True
        result = max(result, dist)
        for i in range(1, n + 1):
            if graph[v][i] != 0 and not visited[i]:
                q.append((i, dist + graph[v][i]))


n = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

result = 0

for i in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

bfs(1)

print(result)
