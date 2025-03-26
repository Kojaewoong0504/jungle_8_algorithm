import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

# 값과 인덱스를 함께 저장하고 정렬
indexed_numbers = [(num, i) for i, num in enumerate(numbers)]
indexed_numbers.sort()  # 값 기준으로 정렬

good_count = 0
for i in range(n):
    target = numbers[i]
    is_good = False

    for j in range(n):
        if j == i:  # 같은 위치의 수는 사용할 수 없음
            continue

        complement = target - numbers[j]

        # 이분 탐색으로 complement 찾기
        pos = bisect_left(indexed_numbers, (complement, -1))

        # 찾은 위치부터 같은 값이 있는지 확인
        while pos < n and indexed_numbers[pos][0] == complement:
            k = indexed_numbers[pos][1]  # 원래 배열에서의 인덱스
            if k != i and k != j:  # i와 j가 아닌 다른 위치인지 확인
                is_good = True
                break
            pos += 1

        if is_good:
            break

    if is_good:
        good_count += 1

print(good_count)
