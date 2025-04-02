import sys

import heapq

input = sys.stdin.readline

n, m, k = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

interview_cities = list(map(int, input().split()))

# 그래프 방향 뒤집기
reversed_graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    for next_node, weight in graph[i]:
        reversed_graph[next_node].append((i, weight))


# 뒤집은 그래프에서 다익스트라 실행
def dijkstra_reversed():
    distance = [float('inf')] * (n + 1)
    q = []

    # 모든 면접장을 시작점으로 설정
    for city in interview_cities:
        distance[city] = 0
        heapq.heappush(q, (0, city))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for next_node, weight in reversed_graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    return distance


# 최단 거리 계산
distances = dijkstra_reversed()

# 가장 먼 도시 찾기
max_distance = -1
max_city = -1

for city in range(1, n + 1):
    if distances[city] != float('inf') and distances[city] > max_distance:
        max_distance = distances[city]
        max_city = city
    elif distances[city] == max_distance and city < max_city:
        max_city = city

print(max_city)
print(max_distance)
