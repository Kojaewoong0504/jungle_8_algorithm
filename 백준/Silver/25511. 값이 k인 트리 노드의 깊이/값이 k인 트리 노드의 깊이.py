from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)

datas = list(map(int, input().split()))
target = datas.index(k)

depth = [-1] * n
depth[0] = 0
q = deque([0])

while q:
    u = q.popleft()
    for v in graph[u]:
        depth[v] = depth[u] + 1
        q.append(v)

print(depth[target])