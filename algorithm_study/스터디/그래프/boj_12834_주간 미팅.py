import heapq


def dijkstra(start, distance):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (distance[start], start))

    while queue:
        dist, node = heapq.heappop(queue)

        if distance[node] < dist:
            continue

        for n_node, c in graph[node]:
            cost = dist + c
            if cost < distance[n_node]:
                distance[n_node] = cost
                heapq.heappush(queue, (cost, n_node))


n, v, e = map(int, input().split())
a, b = map(int, input().split())
houses = list(map(int, input().split()))

graph = [[] for _ in range(v + 1)]

for _ in range(e):
    pa, pb, l = map(int, input().split())
    graph[pa].append((pb, l))
    graph[pb].append((pa, l))

total_dis = 0

for i in range(n):
    k = 0
    f = 0

    INF = float('INF')
    distances = [INF] * (v + 1)
    dijkstra(houses[i], distances)
    if distances[a] == INF:
        k = -1
    if distances[b] == INF:
        f = -1
    if distances[a] != INF:
        k = distances[a]
    if distances[b] != INF:
        f = distances[b]

    total_dis = total_dis + k + f

print(total_dis)
