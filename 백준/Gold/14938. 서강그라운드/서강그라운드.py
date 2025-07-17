import sys
import heapq
input = sys.stdin.readline

n, m, r = map(int, input().split())
t = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for i in range(r):
    a, b, l = map(int, input().split())
    graph[a - 1].append((b - 1, l))
    graph[b - 1].append((a - 1, l))

INF = float('inf')


def dijkstra(start):
    distance = [INF] * n
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node, length in graph[now]:
            cost = dist + length
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))
    total = 0
    for i in range(n):
        if distance[i] <= m:
            total += t[i]
    return total


max_item = 0
for i in range(n):
    cnt = dijkstra(i)
    max_item = max(max_item, cnt)

print(max_item)
