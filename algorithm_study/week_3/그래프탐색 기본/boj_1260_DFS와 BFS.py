from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)


def dfs(node):
    visited[node] = True
    print(str(node), end=" ")
    for i in range(1, n+1):
        if graph[node][i] == 1 and not visited[i]:
            dfs(i)



def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = True
    while q:
        now = q.popleft()
        print(str(now), end=" ")
        for i in range(1, n+1):
            if graph[now][i] == 1 and not visited[i]:
                q.append(i)
                visited[i] = True


for _ in range(m):
    src, dst = map(int, input().split())
    graph[src][dst] = 1
    graph[dst][src] = 1

dfs(v)
print('')
visited = [False] * (n+1)
bfs(v)