import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
pos = sorted(list(map(int, input().split())))

if k >= n:
    print(0)
    sys.exit()

x = []

for i in range(1, n):
    x.append(pos[i] - pos[i - 1])

for _ in range(k - 1):
    x[x.index(max(x))] = 0

print(sum(x))