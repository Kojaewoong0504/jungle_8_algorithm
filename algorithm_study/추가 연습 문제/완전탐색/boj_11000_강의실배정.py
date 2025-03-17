import sys
import heapq

input = sys.stdin.readline

n = int(input())
study_list = [[*map(int, input().split())] for _ in range(n)]
study_list.sort(key=lambda x: (x[0], x[1]))

heap = [study_list[0][1]]
for i in range(1,n):
    if heap[0] <= study_list[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap,study_list[i][1])

print(len(heap))