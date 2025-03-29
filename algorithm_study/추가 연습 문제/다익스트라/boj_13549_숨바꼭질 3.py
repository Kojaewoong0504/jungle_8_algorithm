from collections import deque

n, k = map(int, input().split())

limit = 100001
cnt = [0] * limit
visited = [False] * limit

def bfs(x, end):
    q = deque()
    q.append(x)

    while q:
        now = q.popleft()
        if now == end:
            return cnt[now]
        if -1 < now * 2 < limit and not visited[now * 2]:
            q.appendleft(now * 2)
            cnt[now * 2] = cnt[now]
            visited[now * 2] = True
        if -1 < now - 1 < limit and not visited[now - 1]:
            q.append(now - 1)
            cnt[now - 1] = cnt[now] + 1
            visited[now - 1] = True
        if -1 < now + 1 < limit and not visited[now + 1]:
            q.append(now + 1)
            cnt[now + 1] = cnt[now] + 1
            visited[now + 1] = True


print(bfs(n,k))