# 이진 탐색 구현
n = int(input())
num_list = list(map(int, input().split()))

lis = [num_list[0]]

def binary_search(lis, target):
    start = 0
    end = len(lis)
    while start <= end:
        mid = (start + end) // 2
        if lis[mid] == target:
            return mid
        elif lis[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return start

for i in range(1,n):
    if num_list[i] > lis[-1]:
        lis.append(num_list[i])
    else:
        lis[binary_search(lis, num_list[i])] = num_list[i]

print(len(lis))

# bisect 사용 사례
from bisect import bisect_left

n = int(input())
num_list = list(map(int, input().split()))

lis = [num_list[0]]

for i in range(1,n):
    if num_list[i] > lis[-1]:
        lis.append(num_list[i])
    else:
        lis[bisect_left(lis,num_list[i])] = num_list[i]

print(len(lis))