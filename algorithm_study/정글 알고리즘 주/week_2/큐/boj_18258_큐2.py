import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

order_list = []

for _ in range(n):
    order = list(map(str, input().split()))
    order_list.append((order[0], order[1:]))

q = deque()

for orders in order_list:
    order = orders[0]
    num = int(*orders[1])

    if order == "push":
        q.append(num)
    elif order == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif order == "size":
        print(len(q))
    elif order == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif order == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif order == "back":
        if q:
            print(q[-1])
        else:
            print(-1)