import heapq
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]


def dijkstra(start_nodes):
    dist = [INF] * (n + 1)
    hq = []
    for s in start_nodes:
        dist[s] = 0
        heapq.heappush(hq, (0, s))

    while hq:
        d, node = heapq.heappop(hq)
        if d > dist[node]:
            continue
        for nei, cost in graph[node]:
            if dist[nei] > d + cost:
                dist[nei] = d + cost
                heapq.heappush(hq, (dist[nei], nei))
    return dist


for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

fans = list(map(int, input().split()))
INF = float('inf')
idol_dist = dijkstra([1])
fan_dist = dijkstra(fans)

result = []

for i in range(2, n + 1):
    if idol_dist[i] < fan_dist[i]:
        result.append(i)

print(" ".join(map(str, sorted(result))) if result else "0")
