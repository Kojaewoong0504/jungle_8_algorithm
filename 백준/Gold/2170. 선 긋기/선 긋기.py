import sys
input = sys.stdin.readline
n = int(input())

lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append([a, b])
lines.sort(key=lambda x : x[0]) # 시작점으로 오름차순 정렬

start, end = lines[0][0], lines[0][1]
answer = 0 # 선들의 합
for i in range(1, n):
    if lines[i][0] <= end and lines[i][1] <= end: # 완전 겹치는 경우
        continue
    elif lines[i][0] <= end and lines[i][1] > end: # 약간 겹치는 경우
        end = lines[i][1]
    else: # 아예 안겹치는 경우
        answer += end - start
        start = lines[i][0]
        end = lines[i][1]
answer += end-start
print(answer)