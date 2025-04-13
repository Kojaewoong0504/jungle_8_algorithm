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