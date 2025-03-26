import heapq

n = int(input())
heap_data = []
for _ in range(n):
    order = list(map(int, input().split()))
    if order[0] != 0:
        for gift in order[1:]:
            heapq.heappush(heap_data, -gift)
    else:
        if heap_data:
            print(-heapq.heappop(heap_data))
        else:
            print(-1)
