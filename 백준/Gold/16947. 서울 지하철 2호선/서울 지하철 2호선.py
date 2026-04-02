from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)

for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    degree[a] += 1
    degree[b] += 1

removed = [False] * (N + 1)
q = deque()

for i in range(1, N + 1):
    if degree[i] == 1:
        q.append(i)

while q:
    cur = q.popleft()
    removed[cur] = True

    for nxt in graph[cur]:
        if removed[nxt]:
            continue
        degree[nxt] -= 1
        if degree[nxt] == 1:
            q.append(nxt)

dist = [-1] * (N + 1)
q = deque()

for i in range(1, N + 1):
    if not removed[i]:
        dist[i] = 0
        q.append(i)

while q:
    cur = q.popleft()

    for nxt in graph[cur]:
        if dist[nxt] != -1:
            continue
        dist[nxt] = dist[cur] + 1
        q.append(nxt)

print(*dist[1:])