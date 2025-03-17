import sys
import heapq
input = sys.stdin.readline
n, k = map(int,input().split())
mv = []
c = []

for _ in range(n):
    mv.append(list(map(int, input().split())))
for _ in range(k):
    c.append(int(input()))

mv.sort()
c.sort()
result = 0
tmp = []

for bag in c:
    while mv and mv[0][0] <= bag:
        heapq.heappush(tmp, -mv[0][1])
        heapq.heappop(mv)
    if tmp:
        result -= heapq.heappop(tmp)
print(result)

