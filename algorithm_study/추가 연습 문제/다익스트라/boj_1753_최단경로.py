import heapq

v, e = map(int, input().split())
start = int(input())

INF = float('inf')  # 무한대 값 설정
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # 방향 그래프이므로 단방향으로만 추가


def dijkstra(start):
    distance = [INF] * (v + 1)
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


ans = dijkstra(start)

for i in range(1, v + 1):
    if ans[i] == INF:
        print("INF")
    else:
        print(ans[i])
