from collections import deque
import sys

input = sys.stdin.readline
t = int(input())


for _ in range(t):
    n = int(input())
    rank = list(map(int, input().split()))
    in_degree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    is_possible = True
    for i in range(n):
        in_degree[rank[i]] = i
        graph[rank[i]] = rank[i+1:]

    m = int(input())

    for _ in range(m):
        a, b = map(int, input().split())
        if b in graph[a]:
            in_degree[a] += 1
            in_degree[b] -= 1
            graph[b].append(a)
            graph[a].remove(b)
        else:
            graph[b].remove(a)
            graph[a].append(b)
            in_degree[a] -= 1
            in_degree[b] += 1

    q = deque()
    result = []
    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)
    if any(in_degree):
        print("IMPOSSIBLE")
    else:
        for v in result:
            print(v, end = ' ')
        print()
