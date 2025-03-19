import sys
input = sys.stdin.readline
n = int(input())

def roundUp(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

if n == 0:
    print(0)
else:
    rank_list = []
    for _ in range(n):
        rank_list.append(int(input().rstrip()))
    rank_list.sort()
    cal_fifteen_per_people = roundUp(n * 0.15)
    slice_data = rank_list[cal_fifteen_per_people:n - cal_fifteen_per_people]
    print(roundUp(sum(slice_data) / len(slice_data)))
