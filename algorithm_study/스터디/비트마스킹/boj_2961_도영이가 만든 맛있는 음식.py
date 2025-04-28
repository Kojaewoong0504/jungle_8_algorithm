import sys
input = sys.stdin.readline

n = int(input())

item_list = [list(map(int, input().split())) for _ in range(n)]

min_result = float('INF')

for i in range(1, 1 << n):
    sour = 1
    acerbity = 0

    for j in range(n):
        if i & (1 << j):
            sour *= item_list[j][0]
            acerbity += item_list[j][1]
    min_result = min(min_result, abs(sour - acerbity))

print(min_result)