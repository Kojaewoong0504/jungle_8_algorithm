import sys
from collections import deque

input = sys.stdin.readline

a, b, n, m = map(int, input().split())
graph = [0 for _ in range(100001)]
visited = [False for _ in range(100001)]


def bfs(x):
    dy = [1, -1, a, -a, b, -b, a, b]
    q = deque([x])
    visited[x] = True
    while q:

        target = q.popleft()

        for i in range(8):
            if i < 6:

                y = target + dy[i]
                if 0 <= y <= 100000 and not visited[y]:
                    q.append(y)
                    visited[y] = True
                    graph[y] = graph[target] + 1

            else:
                y = target * dy[i]
                if 0 <= y <= 100000 and not visited[y]:
                    q.append(y)
                    visited[y] = True
                    graph[y] = graph[target] + 1


bfs(n)

print(graph[m])
