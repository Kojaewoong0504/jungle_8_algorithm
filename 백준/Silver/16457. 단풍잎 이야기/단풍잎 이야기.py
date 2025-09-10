from itertools import combinations

import sys

n, m, k = map(int, sys.stdin.readline().strip().split())

nums = set()
data = []
for _ in range(m):
    skills = tuple(map(int, sys.stdin.readline().strip().split()))
    data.append(skills)
    nums.update(skills)

max_count = 0
if len(nums) <= n:
    comb = tuple(nums)
    count = 0
    for num in data:
        if all(x in comb for x in num):
            count += 1
    max_count = max(max_count, count)
else:
    for comb in combinations(nums, n):
        count = 0
        for num in data:
            if all(x in comb for x in num):
                count += 1
        max_count = max(count, max_count)

print(max_count)