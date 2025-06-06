import heapq as hq

n, m = map(int, input().split())
present = []

for x in list(map(int, input().split())):
    hq.heappush(present, -x)
wish = list(map(int, input().split()))

not_enough_present = False
for i in wish:
    x = -hq.heappop(present)
    if x - i < 0:
        not_enough_present = True
        break
    hq.heappush(present, -(x - i))

if not_enough_present:
    print(0)
else:
    print(1)
