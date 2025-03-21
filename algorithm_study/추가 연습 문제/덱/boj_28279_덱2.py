from collections import deque

n = int(input())

orders = []

for _ in range(n):
    orders.append(list(map(int,input().split())))

q = deque()

for i in range(n):
    order, num = 0, 0

    if len(orders[i]) > 1:
        num = orders[i][1]
    order = orders[i][0]
    if order == 1:
        q.appendleft(num)
    elif order == 2:
        q.append(num)
    elif order == 3:
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif order == 4:
        if q:
            print(q.pop())
        else:
            print(-1)
    elif order == 5:
        print(len(q))
    elif order == 6:
        if q:
            print(0)
        else:
            print(1)
    elif order == 7:
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)