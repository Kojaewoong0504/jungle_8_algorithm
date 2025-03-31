import sys
from collections import deque

input = sys.stdin.readline
t = int(input())


for _ in range(t):
    check = [False for _ in range(10001)]
    start, end = map(int, input().split())

    q = deque()
    q.append([start, ''])
    check[start] = True

    while q:
        n, cmd = q.popleft()

        if n == end:
            print(cmd)
            break

        # D
        d = (n * 2) % 10000
        if not check[d]:
            check[d] = True
            q.append([d, cmd + 'D'])

        # S
        s = (n - 1) % 10000
        if not check[s]:
            check[s] = True
            q.append([s, cmd + 'S'])

        # L
        l = n // 1000 + (n % 1000) * 10
        if not check[l]:
            check[l] = True
            q.append([l, cmd + 'L'])

        # R
        r = n // 10 + (n % 10) * 1000
        if not check[r]:
            check[r] = True
            q.append([r, cmd + 'R'])
