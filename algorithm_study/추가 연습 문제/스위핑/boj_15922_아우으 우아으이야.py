import sys

input = sys.stdin.readline
n = int(input())

lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort()

total = abs(lines[0][0] - lines[0][1])
now_end = lines[0][1]
for i in range(1, len(lines)):
    if lines[i][0] <= now_end <= lines[i][1]:
        total += abs(lines[i][1] - now_end)
        now_end = lines[i][1]
    if lines[i][0] >= now_end:
        total += abs(lines[i][0] - lines[i][1])
        now_end = lines[i][1]

print(total)
