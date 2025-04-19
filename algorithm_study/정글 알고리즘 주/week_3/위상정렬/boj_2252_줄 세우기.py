import sys
from collections import deque
input = sys.stdin.readline

def topology(N,comparisons):
    indegree = [0] * (N+1) #진입차수
    graph =[[] for _ in range(N+1)]

    for comparison in comparisons:
        A,B = comparison
        graph[A].append(B)
        indegree[B] += 1

    result = []
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        current = q.popleft()
        result.append(current)

        for next_node in graph[current]:
            indegree[next_node] -= 1

            if indegree[next_node] == 0:
                q.append(next_node)

    return result


N, M = map(int, input().split())
comparisons = [tuple(map(int, input().split())) for _ in range(M)]

order = topology(N, comparisons)
print(*order)