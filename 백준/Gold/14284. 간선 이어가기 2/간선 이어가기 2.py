import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

limit = float("INF")
graph = [[] for _ in range(n+1)]
distance = [limit] * (n+1)


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

start, end = map(int, input().split())


def dijkstra(s, e):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, node = heapq.heappop(q)

        if dist > distance[node]:
            continue

        for u, v in graph[node]:
            cost = dist +v
            if cost < distance[u]:
                distance[u] = cost
                heapq.heappush(q, (cost, u))
    return distance[e]

print(dijkstra(start, end))