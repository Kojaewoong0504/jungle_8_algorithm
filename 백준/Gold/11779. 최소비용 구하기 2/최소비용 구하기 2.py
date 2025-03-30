import heapq
import sys

input = sys.stdin.readline


n = int(input())
m = int(input())
INF = int(1e18)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a].append((b,c))

start, end = map(int, input().split())
distance = [INF] * (n+1)
prev_node = [start] * (n+1)


def dijkstra(start):

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for v, w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                prev_node[v] = now
                heapq.heappush(q, (cost, v))

dijkstra(start)

ans = []
tmp = end
while tmp != start:
    ans.append(str(tmp))
    tmp = prev_node[tmp]

ans.append(str(start))
ans.reverse()

print(distance[end])
print(len(ans))
print(" ".join(ans))