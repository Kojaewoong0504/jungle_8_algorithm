n = int(input())
first, second = map(int,input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(x, count):
    global flag
    visited[x] = True
    if x == second:
        flag = True
        print(count)
    for val in graph[x]:
        if visited[val] == False:
            dfs(val, count+1)


flag = False
dfs(first,0)
if flag == False:
    print(-1)