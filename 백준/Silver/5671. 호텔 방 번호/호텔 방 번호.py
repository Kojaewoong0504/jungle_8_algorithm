import sys
input = sys.stdin.readline

while 1:
    data = input().rstrip()
    if not data:
        break
    res = 0
    a, b = data.split()
    for i in range(int(a), int(b) + 1):
        if len(set(str(i))) == len(str(i)):
            res += 1
    print(res)
