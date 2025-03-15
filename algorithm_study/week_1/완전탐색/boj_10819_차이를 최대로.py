from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
max_sum = -float('INF')

for i in permutations(arr, n):
    cal_result = 0
    for j in range(n-1):
        cal_result += abs(i[j] - i[j+1])
    max_sum = max(max_sum, cal_result)

print(max_sum)



