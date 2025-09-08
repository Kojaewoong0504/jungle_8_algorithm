import sys
input = sys.stdin.readline

N = int(input().strip())
rows = [int(input().strip()) for _ in range(N)]

MAX_R = 1000
avail = [0] * (MAX_R + 1)  # avail[r]: 행 r가 비워지는 가장 이른 시각
answer = 0

for R in rows:
    t = 0
    # 1 ~ R-1 행 통과 (각 1초, 단 다음 행이 비어야 이동 가능)
    for r in range(1, R):
        start = max(t, avail[r])
        finish = max(start + 1, avail[r + 1])  # 다음 행이 비지 않으면 대기 -> 현재 행을 계속 점유
        avail[r] = finish
        t = finish
    # 목적 행 R: 짐 넣기 5초
    start = max(t, avail[R])
    finish = start + 5
    avail[R] = finish
    if finish > answer:
        answer = finish

print(answer)
