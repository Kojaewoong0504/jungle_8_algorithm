import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        friend = q.popleft()
        for i in range(1, n + 1):
            if graph[friend][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[friend] + 1

bfs(1)

result = 0
for i in range(2, n + 1):
    if visited[i] < 4 and visited[i] != 0:
        result += 1

print(result)
