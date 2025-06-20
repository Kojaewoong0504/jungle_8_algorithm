from collections import deque
import sys

input = sys.stdin.readline

n = int(input().strip())
MAX = n

# 1) BFS 로 최단 일수 dist[] 구하기
dist = [-1] * (MAX + 1)
q = deque([0])
dist[0] = 0

while q:
    x = q.popleft()
    d = dist[x]
    if x == n:
        break
    for w, nx in [(1, x + 1), (3, x * 3), (5, x * x)]:
        if nx > MAX:
            continue
        if dist[nx] == -1:
            dist[nx] = d + 1
            q.append(nx)

D = dist[n]

INF = 10**18
prev = [INF] * (MAX+1)
prev[0] = 0

for day in range(1, D+1):
    curr = [INF] * (MAX+1)
    for x in range(MAX+1):
        if prev[x] == INF:
            continue
        # 물 1
        if x+1 <= MAX:
            curr[x+1] = min(curr[x+1], prev[x] + 1)
        # 물 3
        if x*3 <= MAX:
            curr[x*3] = min(curr[x*3], prev[x] + 3)
        # 물 5
        if x*x <= MAX:
            curr[x*x] = min(curr[x*x], prev[x] + 5)
    prev = curr

min_water = prev[n]
print(D, min_water)