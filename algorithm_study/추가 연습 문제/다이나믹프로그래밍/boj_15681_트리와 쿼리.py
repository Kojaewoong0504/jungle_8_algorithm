from function_visualizer import FunctionVisualizer
import sys
sys.setrecursionlimit(100005)
input = sys.stdin.readline


visualizer = FunctionVisualizer()

n, r, q = map(int, input().split())
con = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    con[x].append(y)
    con[y].append(x)

dy = [0] * (n + 1)


@visualizer.visualize(param_names=["d_x", "prev"])
def dfs(d_x, prev):
    global dy
    dy[d_x] = 1
    for ny in con[d_x]:
        if ny == prev: continue
        dfs(ny, d_x)
        dy[d_x] += dy[ny]

dfs(r, -1)

for _ in range(q):
    print(dy[int(input())])


visualizer.render("DFS")
