from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
shot_place = sorted(list(map(int, input().split())))

animal_point = []

for _ in range(n):
    animal_point.append(tuple(map(int, input().split())))

result = 0

for i in range(n):
    x, y = animal_point[i]
    if y > l:
        continue

    left_bound = x - (l - y)
    right_bound = x + (l - y)

    left_idx = bisect_left(shot_place, left_bound)
    right_idx = bisect_right(shot_place, right_bound)

    if right_idx > left_idx:
        result += 1

print(result)