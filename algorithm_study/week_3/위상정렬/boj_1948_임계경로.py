import sys
input = sys.stdin.readline
from collections import deque

def topology_sort():
    q = deque()
    q.append(st)
    while q:
        cur = q.popleft()
        for n_node, w in info[cur]:
            degree[n_node] -= 1
            v = dist[cur] + w
            if dist[n_node] < v:
                dist[n_node] = v
            if degree[n_node] == 0:
                q.append(n_node)
    return dist[en]

def back():
    cnt = 0
    q = deque()
    q.append(en)
    check = [False] * (N+1)
    while q:
        cur = q.popleft()
        for n_node, w in b_info[cur]:
            if dist[cur] - dist[n_node] == w:
                cnt += 1
                if not check[n_node]:
                    check[n_node] = True
                    q.append(n_node)
    return cnt


N = int(input())
M = int(input())
info = [[] for _ in range(N+1)]
b_info = [[] for _ in range(N+1)]
degree = [0] * (N+1)
for _ in range(M):
    a, b, c = map(int, input().split())
    info[a].append((b, c))
    b_info[b].append((a, c))
    degree[b] += 1
st, en = map(int, input().split())
dist = [0] * (N+1)
print(topology_sort())
print(back())