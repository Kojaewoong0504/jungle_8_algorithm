import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(node):
    visited[node] = True
    for i in range(1, n+1):
        if graph[node][i] == 1 and not visited[i]:
            dfs(i)


cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        visited[i] = True
        dfs(i)
        cnt += 1

print(cnt)