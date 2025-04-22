import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
friend = [[] for _ in range(n+1)]


for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)


def bfs(friend, start):
    num = [0] * (n+1)
    find[start] = 1

    q = deque()
    q.append(start)

    while q:
        x = q.popleft()
        for i in friend[x]:
            if find[i] == 0:
                num[i] = num[x] + 1
                find[i] = 1
                q.append(i)
    return sum(num)

result = []

for i in range(1,n+1):
    find = [0] * (n+1)
    result.append(bfs(friend, i))

print(result.index(min(result)) + 1)