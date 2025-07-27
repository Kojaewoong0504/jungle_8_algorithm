# from heapq import heappush, heappop
# import sys
# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline
#
#
# N = int(input())
# T, M = map(int, input().split())
# L = int(input())
#
# INF = int(1e9)
# graph = [[] for _ in range(N + 1)]
#
# for _ in range(L):
#     a, b, time, cost = map(int, input().split())
#     graph[a].append((b, time, cost))
#     graph[b].append((a, time, cost))
#
# distcost = [[INF for _ in range(10000 + 1)] for _ in range(N + 1)]
# distcost[1][0] = 0
#
# q = [(0, 0, 1)]
# while q:
#     time, cost, now = heappop(q)
#     if distcost[now][cost] < time:
#         continue
#     for nxt, n_t, n_c in graph[now]:
#         tt, tc = time + n_t, cost + n_c
#         if tt <= T and tc <= M:
#             if tt < distcost[nxt][tc]:
#                 distcost[nxt][tc] = tt
#                 heappush(q, (tt, tc, nxt))
#
# for i in range(M + 1):
#     if distcost[N][i] <= T:
#         print(i)
#         sys.exit()
# print(-1)

import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def dfs(node, T, C):
    global answer

    if node == n - 1:
        answer = min(answer, C)
        return
    for nxt, time, cost in graph[node]:
        if not visited[nxt]:
            if T + time <= t and C + cost <= m:
                visited[nxt] = True
                dfs(nxt, T + time, C + cost)
                visited[nxt] = False


n = int(input())
t, m = map(int, input().split())
l = int(input())
INF = int(1e9)

graph = [[] for _ in range(n)]
for _ in range(l):
    a, b, time, cost = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, time, cost))
    graph[b].append((a, time, cost))

answer = INF
visited = [False] * n
visited[0] = True
dfs(0, 0, 0)
if answer == INF:
    print(-1)
else:
    print(answer)
