import sys
sys.setrecursionlimit(10**6)

n, t = map(int, input().split())
pointers = [0] + list(map(int, input().split()))
visited = {}
path = []

cur = 1
while cur not in visited:
    visited[cur] = len(path)
    path.append(cur)
    cur = pointers[cur]

cycle_start = visited[cur]
cycle_length = len(path) - cycle_start

if t < cycle_start:
    print(path[t])
else:
    t_in_cycle = (t - cycle_start) % cycle_length
    print(path[cycle_start + t_in_cycle])

