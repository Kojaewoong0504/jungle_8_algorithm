import sys
from collections import deque

input = sys.stdin.readline

n, c = map(int, input().split())

portal_type = [-1] * n
pend = [-1] * n

for _ in range(c):
    t, a, b = map(int, input().split())
    portal_type[a] = t
    pend[a] = b

INF = 10 ** 18
dist = [INF] * n
dist[0] = 0

q = deque([0])

while q:
    x = q.popleft()
    if x == n - 1:
        break

    t = portal_type[x]

    if t == -1:
        nx = x + 1
        if nx < n and dist[nx] > dist[x] + 1:
            dist[nx] = dist[x] + 1
            q.append(nx)

    elif t == 0:
        nx = pend[x]
        if 0 <= nx < n and dist[nx] > dist[x]:
            dist[nx] = dist[x]
            q.appendleft(nx)

    else:
        nx = pend[x]
        if 0 <= nx < n and dist[nx] > dist[x]:
            dist[nx] = dist[x]
            q.appendleft(nx)
        nx2 = x + 1
        if nx2 < n and dist[nx2] > dist[x] + 1:
            dist[nx2] = dist[x] + 1
            q.append(nx2)


print(-1 if dist[n - 1] == INF else dist[n - 1])