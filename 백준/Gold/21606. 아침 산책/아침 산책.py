import sys

input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().strip()))

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

total = 0

for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

    if a[x] == 1 and a[y] == 1:
        total += 2


def dfs(node, cnt):
    visited[node] = True
    for i in graph[node]:
        if a[i] == 1 and not visited[i]:
            cnt += 1
        elif not visited[i] and a[i] == 0:
            cnt += dfs(i, cnt)
    return cnt


for i in range(1, n+1):
    if a[i] == 0 and not visited[i]:
        result = dfs(i, 0)
        total += (result) * (result - 1)

print(total)
