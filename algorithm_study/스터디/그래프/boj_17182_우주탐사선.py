n, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

for m in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][m] + graph[m][j]:
                graph[i][j] = graph[i][m] + graph[m][j]

def dfs(pos, cnt, cost):
    global result
    if cnt == n:
        result = min(result, cost)
        return

    for nxt in range(n):
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, cnt + 1, cost + graph[pos][nxt])
            visited[nxt] = False


visited = [False] * n
result = float('inf')
visited[k] = True

dfs(k, 1, 0)
print(result)