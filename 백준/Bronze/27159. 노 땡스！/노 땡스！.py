import sys
input = sys.stdin.readline

# 입력
n = int(input())
lst = list(map(int, input().split()))

# 점수계산
res = 0
first = lst[0]  # 최초 시작점
pre = lst[0]  # 이전값

for i in lst[1:]:
    # 1씩 오름차순이 끊기면 이전 값 더하기
    if i != pre + 1:
        res += first
        first = i
    pre = i

res += first
print(res)