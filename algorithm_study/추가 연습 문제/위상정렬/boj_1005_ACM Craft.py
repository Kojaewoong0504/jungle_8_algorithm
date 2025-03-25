import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():
    result = times.copy()
    q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    for i in range(1, n+1):
        now = q.popleft()
        result.append(now)

        for next in graph[now]:
            indegree[next] -= 1
            result[next] = max(result[next], result[now] + times[next])
            if indegree[next] == 0:
                q.append(next)
    print(result[target])


for i in range(int(input())):
    n, m = map(int, input().split())
    times = list(map(int, input().split()))
    times.insert(0,0)
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    target = int(input())
    topology_sort()

