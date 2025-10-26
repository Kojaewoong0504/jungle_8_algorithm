import sys

input = sys.stdin.readline
N = int(input().strip())
max_min = 0
max_max = 0
for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a  # a = min, b = max
    if a > max_min:
        max_min = a
    if b > max_max:
        max_max = b

print(max_min * max_max)
