import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

cnt = [0] * 21
q = deque()
ans = 0

for _ in range(n):
    name = input().strip()
    l = len(name)

    if len(q) > k:
        oldL = q.popleft()
        cnt[oldL] -= 1

    ans += cnt[l]

    cnt[l] += 1
    q.append(l)

print(ans)
