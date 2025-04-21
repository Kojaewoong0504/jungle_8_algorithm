n = int(input())

s = 0

for _ in range(n):

    data = input().rstrip().split()

    if data[0] == "add":
        x = int(data[1])
        s |= (1 << (x-1))

    elif data[0] == "remove":
        x = int(data[1])
        s &= ~(1 << (x-1))
    elif data[0] == "check":
        x = int(data[1])
        if s & (1 << (x-1)):
            print(1)
        else:
            print(0)
    elif data[0] == "toggle":
        x = int(data[1])
        s ^= (1 << (x-1))
    elif data[0] == "all":
        s = (1 << 20) - 1
    elif data[0] == "empty":
        s = 0
    