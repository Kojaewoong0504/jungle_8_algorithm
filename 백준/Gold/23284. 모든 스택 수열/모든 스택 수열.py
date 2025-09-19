import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().strip())
out = []
buf = []

def dfs(next_push, stack):
    if len(buf) == n:
        out.append(' '.join(map(str, buf)))
        return
    if stack:
        x = stack.pop()
        buf.append(x)
        dfs(next_push, stack)
        buf.pop()
        stack.append(x)
    if next_push <= n:
        stack.append(next_push)
        dfs(next_push + 1, stack)
        stack.pop()

dfs(1, [])
print('\n'.join(out))
