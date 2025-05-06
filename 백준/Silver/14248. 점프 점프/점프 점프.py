import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
b = list(map(int, input().split()))
s = int(input())
cnt = 1
visited = [False] * n


def dfs(x):
    global cnt
    for nx in (x + b[x], x - b[x]):
        if 0 <= nx < n and not visited[nx]:
            cnt += 1
            visited[nx] = True
            dfs(nx)


dfs(s - 1)
print(cnt)
