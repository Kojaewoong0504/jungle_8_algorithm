n, m = map(int,input().split())


INF = float('INF')
graph = [[INF for _ in range(n+1)] for _  in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]


min_sum = INF
answer = 0
for i in range(1, n + 1):
    total = sum(graph[i][1:])
    if total < min_sum:
        min_sum = total
        answer = i
print(answer)