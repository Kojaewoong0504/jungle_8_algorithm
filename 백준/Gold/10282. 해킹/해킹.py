import sys
import heapq

input = sys.stdin.readline

t = int(input())
INF = 10 ** 15

def dijkstra(start, graph):
    n = len(graph)
    dists = [INF] * n
    dists[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dists[now] < dist:
            continue

        for node, time in graph[now]:
            cost = dist + time
            if cost < dists[node]:
                dists[node] = cost
                heapq.heappush(q, (cost, node))
    return dists

for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        a -= 1; b -= 1
        graph[b].append((a, s))

    answer = dijkstra(c - 1, graph)
    send_time = []
    for time in answer:
        if time != INF:
            send_time.append(time)
    count = len(send_time)
    last_time = max(send_time) if send_time else 0

    print(count, last_time)