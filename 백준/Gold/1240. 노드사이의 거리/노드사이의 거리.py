import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]


for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

want = []
for _ in range(m):
    want.append(list(map(int, input().split())))

INF = 10**9
def dijkstra(start, end):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if now == end:  # 목적지에 도달하면 바로 반환
            return dist

        if dist > distance[now]:
            continue

        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    return distance[end]

for start, end in want:
    result = dijkstra(start, end)
    print(result)