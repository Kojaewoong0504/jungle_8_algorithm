import sys
import copy

input = sys.stdin.readline

n = int(input())
items = [list(map(int, input().split())) for _ in range(n)]


first = copy.deepcopy(items)
second = copy.deepcopy(items)

first.sort(key=lambda x: (-x[0], x[1]))
second.sort(key=lambda x: (x[1], -x[0]))

print(f"{first[0][0]} {first[0][1]} {first[1][0]} {first[1][1]}")
print(f"{second[0][0]} {second[0][1]} {second[1][0]} {second[1][1]}")