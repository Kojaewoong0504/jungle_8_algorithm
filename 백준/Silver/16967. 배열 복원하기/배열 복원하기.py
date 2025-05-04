import sys

input = sys.stdin.readline

h, w, x, y = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h + x)]
for i in range(x, h):
    for j in range(y, w):
        b[i][j] = b[i][j] - b[i - x][j - y]

for result in b[:h]:
    print(*result[:w])
