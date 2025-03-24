import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visits = list(map(int, input().split()))

if max(visits) == 0:
    print("SAD")
    exit(0)

value = sum(visits[:x])
max_value = value
cnt = 1
for i in range(x, n):
    value += visits[i]
    value -= visits[i-x]
    if value > max_value:
        max_value = value
        cnt = 1
    elif value == max_value:
        cnt += 1
print(max_value)
print(cnt)