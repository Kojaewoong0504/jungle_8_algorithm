import sys
from math import sqrt

input = sys.stdin.readline
n, k = map(int, input().split())
priority_nums = list(map(int, input().split()))
min_data = float('INF')

def standard(nums, k):
    average = sum(nums) / k
    cal = 0
    for num in nums:
        cal = cal + (num - average)**2
    cal = cal / k
    cal2 = sqrt(cal)
    return cal2


for i in range(k, len(priority_nums)+1):
    for j in range(0, (len(priority_nums)-k+1)):
        if j + i <= len(priority_nums):
            min_data = min(min_data, standard(list(priority_nums[j:j+i]), i))

print(min_data)