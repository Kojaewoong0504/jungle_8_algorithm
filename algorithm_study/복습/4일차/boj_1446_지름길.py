import heapq


n, m = map(int, input().split())

graph = [[] for _ in range(m+1)]
INF = 10**8

def dijkstra(start):
    distance = [INF] * (m+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue

        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return distance

for i in range(m):
    graph[i].append((i+1,1))

for _ in range(n):
    a, b, c = map(int, input().split())
    if b > m:
        continue
    graph[a].append((b, c))

result = dijkstra(0)
print(result[m])