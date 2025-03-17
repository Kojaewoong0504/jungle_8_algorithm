import sys

input = sys.stdin.readline

m = int(input())
S = 0  # 비트마스크로 집합 표현

for _ in range(m):
    cmd = input().strip().split()

    if cmd[0] == "add":
        x = int(cmd[1])
        S |= (1 << (x - 1))  # x번째 비트를 1로 설정

    elif cmd[0] == "remove":
        x = int(cmd[1])
        S &= ~(1 << (x - 1))  # x번째 비트를 0으로 설정

    elif cmd[0] == "check":
        x = int(cmd[1])
        if S & (1 << (x - 1)):  # x번째 비트가 1인지 확인
            print(1)
        else:
            print(0)

    elif cmd[0] == "toggle":
        x = int(cmd[1])
        S ^= (1 << (x - 1))  # x번째 비트 토글

    elif cmd[0] == "all":
        S = (1 << 20) - 1  # 모든 비트를 1로 설정

    elif cmd[0] == "empty":
        S = 0  # 모든 비트를 0으로 설정
