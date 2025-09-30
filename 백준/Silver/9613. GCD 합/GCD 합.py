from itertools import combinations
from math import gcd


t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    gcd_data = 0
    for comb in combinations(nums[1:], 2):
        gcd_data += gcd(comb[0], comb[1])
    print(gcd_data)
