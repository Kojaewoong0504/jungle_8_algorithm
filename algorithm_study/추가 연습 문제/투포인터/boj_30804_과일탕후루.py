import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
stick = list(map(int, input().split()))

max_length = 0
fruit_count = defaultdict(int)
unique_fruits = 0
left = 0

for right in range(n):
    # 오른쪽 끝 과일 추가
    fruit_count[stick[right]] += 1
    if fruit_count[stick[right]] == 1:
        unique_fruits += 1

    # 과일 종류가 2개를 초과하면 왼쪽 포인터 이동
    while unique_fruits > 2:
        fruit_count[stick[left]] -= 1
        if fruit_count[stick[left]] == 0:
            unique_fruits -= 1
        left += 1

    # 현재 윈도우 길이 업데이트
    max_length = max(max_length, right - left + 1)

print(max_length)
