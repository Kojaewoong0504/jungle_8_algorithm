import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * (n)
graph = [[] for _ in range(n)]
can_friend = False

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start, depth):
    global can_friend
    visited[start] = True
    if depth == 5:
        can_friend = True
        return
    for i in graph[start]:
        if visited[i] == False:
            dfs(i, depth + 1)
    visited[start] = False


for i in range(n):
    dfs(i, 1)
    if can_friend:
        break

if can_friend:
    print(1)
else:
    print(0)
