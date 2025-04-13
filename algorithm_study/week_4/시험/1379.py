import sys
import heapq

input = sys.stdin.readline

n = int(input())
study_list = [list(map(int, input().split())) for _ in range(n)]
study_list.sort(key=lambda x: (x[1], x[2]))
ans = [0] * (n+1)

room_num = 1
heap = []
heapq.heappush(heap, [study_list[0][2], room_num])

ans = [study_list[0][0]] = room_num

for i in range(1, n):
    pass



#GG
