# import heapq
#
# n = int(input())
#
# heap = []
# num_list = [int(input()) for _ in range(n)]
#
# for i in range(n):
#     heapq.heappush(heap, num_list[i])
#
#     if i == 0:
#         print(heap[i])
#     else:
#         if (i+1) % 2 == 0:
#             print(f"현재 힙{heap}")
#             print(f"선택된 index : {((i+1)//2)-1}, {(i+1)//2}")
#             print(min(heap[((i+1)//2)-1:(i+1)//2]))
#         else:
#             print(f"현재 힙{heap}")
#             print(f"선택된 index : {(i+1)//2}")
#             print(heap[(i+1)//2])

import heapq

n = int(input())
max_heap = []  # 중앙값보다 작은 값들 (최대 힙)
min_heap = []  # 중앙값보다 큰 값들 (최소 힙)

for _ in range(n):
    num = int(input())

    # 힙에 값 추가
    if not max_heap or num <= -max_heap[0]:
        heapq.heappush(max_heap, -num)  # 최대 힙을 위해 음수로 변환
    else:
        heapq.heappush(min_heap, num)

    # 두 힙의 크기 균형 맞추기
    if len(max_heap) < len(min_heap):
        # 최소 힙에서 가장 작은 값을 최대 힙으로 이동
        value = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -value)
    elif len(max_heap) > len(min_heap) + 1:
        # 최대 힙에서 가장 큰 값을 최소 힙으로 이동
        value = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, value)

    # 중앙값 출력 (항상 max_heap의 루트)
    print(-max_heap[0])
