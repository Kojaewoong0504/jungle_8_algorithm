import sys

input = sys.stdin.readline
n = int(input().strip())
data = [tuple(map(int, input().split())) for _ in range(n)]

best_a = best_b = None
best_rss = 1 << 62

for a in range(1, 101):
    for b in range(1, 101):
        rss = 0
        for x, y in data:
            diff = y - (a * x + b)
            rss += diff * diff
            if rss >= best_rss:
                break
        if rss < best_rss:
            best_rss = rss
            best_a, best_b = a, b

print(best_a, best_b)
