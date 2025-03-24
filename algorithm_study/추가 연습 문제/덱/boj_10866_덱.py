import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

orders = [list(map(str, input().split())) for _ in range(n)]
q = deque()
for order in orders:
    o1, o2 = "", 0
    if len(order) > 1:
        o2 = order[1]
    o1 = order[0]
    if o1 == "push_front":
        q.appendleft(o2)
    elif o1 == "push_back":
        q.append(o2)
    elif o1 == "pop_front":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif o1 == "pop_back":
        if q:
            print(q.pop())
        else:
            print(-1)
    elif o1 == "size":
        print(len(q))
    elif o1 == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif o1 == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif o1 == "back":
        if q:
            print(q[-1])
        else:
            print(-1)