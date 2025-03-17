n = int(input())

order_list = []


for _ in range(n):
    order = list(map(str, input().split()))
    order_list.append((order[0], order[1:]))

stack = []

for orders in order_list:
    order = orders[0]
    num = int(*orders[1])

    if order == "push":
        stack.append(num)
    elif order == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif order == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)