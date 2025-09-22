import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

maxdq = deque()  # 값이 내려가도록(앞이 가장 큼), 인덱스 저장
mindq = deque()  # 값이 올라가도록(앞이 가장 작음), 인덱스 저장

ans = 0
l = 0

for r, v in enumerate(A):
    # maxdq: 뒤에서부터 v보다 작은 값 제거 (내림차순 유지)
    while maxdq and A[maxdq[-1]] < v:
        maxdq.pop()
    maxdq.append(r)

    # mindq: 뒤에서부터 v보다 큰 값 제거 (오름차순 유지)
    while mindq and A[mindq[-1]] > v:
        mindq.pop()
    mindq.append(r)

    # 조건 위반 시 왼쪽 포인터 이동
    while A[maxdq[0]] - A[mindq[0]] > 2:
        if maxdq[0] == l:
            maxdq.popleft()
        if mindq[0] == l:
            mindq.popleft()
        l += 1

    ans = max(ans, r - l + 1)

print(ans)

