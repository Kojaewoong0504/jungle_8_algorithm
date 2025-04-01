from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split(" "))
com = [[] for _ in range(n+1)]
for _ in range(m):
    b, a = map(int, input().split(" "))
    com[a].append(b)

def bfs(i):
    q = deque([i])
    visited = [False for _ in range(n+1)]
    visited[i] = True
    cnt = 0
    while q:
        num = q.popleft()
        for nx in com[num]:
            if not visited[nx]:
                cnt += 1
                visited[nx] = True
                q.append(nx)
    return cnt


answer = []
pr = []
for i in range(1,n+1):
    tmp = bfs(i)
    answer.append(tmp)
M = max(answer)    

for j in range(len(answer)):
    if answer[j] == M:
        pr.append(j+1)

print(*pr)
