import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for v, w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q,(cost, v))
    return distance


T = int(input())


for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    INF = int(1e9)
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    targets = []
    for _ in range(t):
        targets.append(int(input()))

    first = dijkstra(s)
    g_dijk = dijkstra(g)
    h_dijk = dijkstra(h)

    result = []

    for target in targets:
        if first[g] + g_dijk[h] + h_dijk[target] == first[target] or first[h] + h_dijk[g] + g_dijk[target] == first[target]:
            result.append(target)

    result.sort()

    for ans in result:
        print(ans, end=" ")
    print()
