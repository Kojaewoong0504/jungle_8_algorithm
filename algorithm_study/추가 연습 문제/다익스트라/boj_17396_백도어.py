import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

wads = list(map(int, input().split()))
wads[-1] = 0
graph = [[] for _ in range(n)]
limit = float("INF")
distance = [limit] * (n)

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b,t))
    graph[b].append((a,t))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for v, time in graph[now]:
            cost = dist + time
            if cost < distance[v] and not wads[v]:
                distance[v] = cost
                heapq.heappush(q, (cost,v))

dijkstra(0)
if distance[n-1] == limit:
    print(-1)
else:
    print(distance[n-1])
