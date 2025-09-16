import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

q = deque()
ins = []

for _ in range(n):
    parts = input().split()  # 공백/개행 모두 안전하게 분리
    if parts[0] == "1":
        q.append(parts[1])   # parts[1]는 이미 'a' 형태
        ins.append(1)        # 뒤에 넣었음을 기록
    elif parts[0] == "2":
        q.appendleft(parts[1])
        ins.append(0)        # 앞에 넣었음을 기록
    else:  # "3"
        if ins:
            last = ins.pop()     # 항상 끝에서 제거 (스택)
            if last == 1:
                q.pop()
            else:
                q.popleft()

if q:
    print("".join(q))
else:
    print(0)
