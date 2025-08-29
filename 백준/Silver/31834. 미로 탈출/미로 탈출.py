import sys
input = sys.stdin.readline

for i in range(int(input())):
    n, s, e = map(int, input().split())

    if (s == 1 and e == n) or (s == n and e == 1):
        print(0)
    elif 1 < s < n:
        if abs(s-e) == 1:
            print(1)
        else:
            print(2)
    elif 1 < e < n:
        print(1)