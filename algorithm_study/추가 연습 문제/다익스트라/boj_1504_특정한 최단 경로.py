import heapq

n, e = map(int, input().split())


graph = [[] for _ in range(n+1)]
INF = 10**8

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

node1, node2 = map(int, input().split())

def dijkstra(start, end):
    distance = [INF] * (n+1)
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
    return distance[end]


cal_data1 = dijkstra(1, node1) + dijkstra(node1,node2) + dijkstra(node2, n)
cal_data2 = dijkstra(1, node2) + dijkstra(node1,node2) + dijkstra(node1, n)
min_data = min(cal_data1,cal_data2)
if min_data >= INF:
    print(-1)
else:
    print(min_data)