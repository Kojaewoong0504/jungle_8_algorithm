import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = []
result = []

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

while q:
    current = heapq.heappop(q)
    result.append(current)
    for next in graph[current]:
        indegree[next] -= 1

        if indegree[next] == 0:
            heapq.heappush(q, next)

print(*result)
