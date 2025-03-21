n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_list.sort()

#1. 이진탐색 구현

def binary_search(start, end, target, data_list):
    while start <= end:
        mid = (start + end) // 2
        if target == data_list[mid]:
            return 1
        elif target < data_list[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in m_list:
    print(binary_search(0, n-1, i, n_list))


#2. python bisect 사용

from bisect import bisect_left, bisect_right
for i in m_list:
    if bisect_left(n_list, i) != (bisect_right(n_list, i)):
        print(1)
    else:
        print(0)
