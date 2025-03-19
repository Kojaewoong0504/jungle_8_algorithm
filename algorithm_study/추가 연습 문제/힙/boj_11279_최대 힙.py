import heapq
import sys
input = sys.stdin.readline

n = int(input())

order_list = []
heap = []

for _ in range(n):
    order_list.append(int(input()))


for order in order_list:
    if order > 0:
        heapq.heappush(heap, -order)
    else:
        if heap:
            result = heapq.heappop(heap)
            print(-1 * result)
        else:
            print(0)