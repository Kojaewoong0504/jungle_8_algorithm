import sys
import heapq
input = sys.stdin.readline

n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]
classes.sort(key=lambda x: x[1])

room = []
cnt = 0
for _class in classes:
    while room and room[0] <= _class[1]:
        heapq.heappop(room)
    heapq.heappush(room, _class[2])
    cnt = max(cnt, len(room))

print(cnt)