import sys
sys.setrecursionlimit(100000)

def dfs(node, dist):
    global max_dist, farthest_node
    if dist > max_dist:
        max_dist = dist
        farthest_node = node
    for next_node, weight in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, dist + weight)

V = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]

for _ in range(V):
    data = list(map(int, sys.stdin.readline().split()))
    u = data[0]
    idx = 1
    while data[idx] != -1:
        v, w = data[idx], data[idx+1]
        graph[u].append((v, w))
        idx += 2

# 1st DFS
visited = [False] * (V+1)
max_dist = 0
farthest_node = 0
visited[1] = True
dfs(1, 0)

# 2nd DFS
visited = [False] * (V+1)
max_dist = 0
visited[farthest_node] = True
dfs(farthest_node, 0)

print(max_dist)
