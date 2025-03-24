from itertools import combinations_with_replacement
import sys

input = sys.stdin.readline


n = int(input())
datas = [list(map(int, input().split())) for _ in range(n)]


for i in range(n):
    cnt = 0
    input_data = datas[i]
    new_datas = [i for i in range(1, max(datas[i])+1)]
    cal_datas = combinations_with_replacement(new_datas, len(datas[i]))
    for j in cal_datas:
        if 1 <= j[0] <= input_data[0] and 1 <= j[1] <= input_data[1] and 1 <= j[2] <= input_data[2]:
            if j[0] % j[1] == j[1] % j[2] == j[2] % j[0]:

                cnt+=1
    print(cnt)