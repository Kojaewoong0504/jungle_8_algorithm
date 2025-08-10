import sys

input = sys.stdin.readline

n, m = map(int, input().split())
snow = [1] + list(map(int, input().split()))

def dfs(size, time, idx):
    global result

    if time > m:
        return

    if time <= m:
        result = max(result, size)

    if idx <= n - 1:
        dfs(size + snow[idx + 1], time + 1, idx + 1)

    if idx <= n - 2:
        dfs((size // 2) + snow[idx + 2], time + 1, idx + 2)


result = 0
dfs(1, 0, 0)
print(result)