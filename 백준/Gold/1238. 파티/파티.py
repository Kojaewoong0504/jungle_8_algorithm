import heapq

n, m, x = map(int,input().split())


INF = 10**8
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))


def dijkstra(start):
    distance = [INF] * (n + 1)
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

memory = [0] * (n+1)

for i in range(1, n+1):
    go_dist = dijkstra(i)
    memory[i] = go_dist[x]

back_dist = dijkstra(x)

max_result = -float('INF')

for i in range(1, n+1):
    max_result = max(max_result, back_dist[i] + memory[i])

print(max_result)