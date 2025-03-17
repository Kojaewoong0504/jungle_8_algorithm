import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    input_num = int(input())
    if input_num == 0:
        if not heap:
            heapq.heappush(heap,input_num)
            print(heapq.heappop(heap))
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, input_num)