from itertools import combinations
import sys

input = sys.stdin.readline
n, m = map(int,input().split())
city = [list(map(int, input().split())) for _ in range(n)]

checkin = []
checkin_comb = []
min_distance = float('INF')
house_list = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            checkin.append((i,j))
        elif city[i][j] == 1:
            house_list.append((i,j))
checkin_comb = combinations(checkin, m)

for cases in checkin_comb:
    dist = [51] * len(house_list)
    for case in cases:
        x, y = case
        for house in range(len(house_list)):
            h_x, h_y = house_list[house]
            house_checkin_dist = abs(h_x-x) + abs(h_y-y)
            dist[house] = min(dist[house], house_checkin_dist)
        min_distance = min(min_distance, sum(dist))

print(min_distance)