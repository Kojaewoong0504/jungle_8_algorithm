import sys
from itertools import combinations
input = sys.stdin.readline

short = [int(input()) for _ in range(9)]

for i in combinations(short, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break