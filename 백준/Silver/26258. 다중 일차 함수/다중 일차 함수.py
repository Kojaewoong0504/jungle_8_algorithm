import sys
import bisect
input = sys.stdin.readline

n = int(input())
xs = []
ys = []
for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

q = int(input())
for _ in range(q):
    k = float(input())
    # k가 들어갈 위치 찾기 (k는 항상 x1 < k < xN, xi와 같지 않음)
    i = bisect.bisect_right(xs, k) - 1
    dy = ys[i+1] - ys[i]
    if dy > 0:
        print(1)
    elif dy < 0:
        print(-1)
    else:
        print(0)
