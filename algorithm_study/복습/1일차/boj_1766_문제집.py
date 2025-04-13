import heapq

n, m = map(int, input().split())

INF = 10**8
graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1


q = []
for i in range(1, n+1):
    if in_degree[i] == 0:
        heapq.heappush(q, i)

while q:
    cur = heapq.heappop(q)
    result.append(cur)

    for i in graph[cur]:
        in_degree[i] -= 1

        if in_degree[i] == 0:
            heapq.heappush(q, i)

print(*result)