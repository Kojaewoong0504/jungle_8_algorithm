import sys
input = sys.stdin.readline

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]

events = []
for x1, x2 in lines:
    events.append((x1, 1))   # 시작
    events.append((x2, -1))  # 끝

# 종료(-1)를 시작(+1)보다 먼저 정렬해야 올바른 처리됨
events.sort(key=lambda x: (x[0], x[1]))

current = 0
max_overlap = 0
for x, delta in events:
    current += delta
    max_overlap = max(max_overlap, current)

print(max_overlap)
