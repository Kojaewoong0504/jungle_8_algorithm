import sys

input = sys.stdin.readline

n, m = map(int, input().split())

trains = [0] * n
MASK = (1 << 20) - 1  # 20비트 유지용 마스크

for _ in range(m):
    input_data = list(map(int, input().split()))
    if len(input_data) == 3:
        cmd, i, x = input_data
        if cmd == 1:
            trains[i - 1] |= (1 << (x - 1))
        elif cmd == 2:
            trains[i - 1] &= ~(1 << (x - 1))

    else:
        cmd, i = input_data
        if cmd == 3:
            trains[i - 1] = (trains[i - 1] << 1) & MASK

        elif cmd == 4:
            trains[i - 1] >>= 1

print(len(set(trains)))
