# import sys
#
# input = sys.stdin.readline
#
# N, weight_list = int(input()), list(map(int, input().split()))
# M, check_list = int(input()), list(map(int, input().split()))
#
# dp = [0]
# for weight in weight_list:
#     tmp = []
#     for i in dp:
#         tmp.append(i + weight)
#         tmp.append(abs(i - weight))
#     dp = list(set((dp + tmp)))
#
# for weight in check_list:
#     if weight in dp:
#         print("Y", end=' ')
#     else:
#         print("N", end=' ')
#
import sys

input = sys.stdin.readline

def cal(num, weight):
    if num > n:
        return
    if d[num][weight]:
        return
    d[num][weight] = True

    cal(num + 1, weight + weights[num - 1])
    cal(num + 1, abs(weight - weights[num - 1]))
    cal(num + 1, weight)


n = int(input())
weights = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))
d = [[False] * 15001 for _ in range(31)]

cal(0, 0)

for t in target:
    if t > 15000:
        print("N", end=" ")
    elif d[n][t]:
        print("Y", end=" ")
    else:
        print("N", end=" ")
