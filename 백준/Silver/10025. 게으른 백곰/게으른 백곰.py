import sys
input = sys.stdin.readline

n, k = map(int, input().split())
buckets = [list(map(int, input().split())) for _ in range(n)]

buckets.sort(key=lambda x: x[1])

max_ice = 0
cur = 0
left = 0

for right in range(n):
    cur += buckets[right][0]
    while buckets[right][1] - buckets[left][1] > 2 * k:
        cur -= buckets[left][0]
        left += 1
    if cur > max_ice:
        max_ice = cur

print(max_ice)