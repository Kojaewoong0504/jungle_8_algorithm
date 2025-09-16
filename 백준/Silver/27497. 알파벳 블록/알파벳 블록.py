import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

q = deque()
ins = []

for _ in range(n):
    parts = input().split()
    if parts[0] in ["1", "2"]:
        if parts[0] == "1":
            q.append(parts[1])
            ins.append(1)
        else:
            q.appendleft(parts[1])
            ins.append(0)
    else:
        if ins:
            last = ins.pop()
            if last == 1:
                q.pop()
            else:
                q.popleft()

if len(q) > 0:
    print("".join(q))
else:
    print(0)