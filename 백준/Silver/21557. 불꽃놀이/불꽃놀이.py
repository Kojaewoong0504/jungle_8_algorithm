import sys

# 입력 받기
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

# 양 끝 폭죽 더미 추출
left = a[0]
right = a[-1]

# N-2번의 연산 중 마지막 연산을 제외한 N-3번 동안 
# 양 끝 더미는 각각 최소 1씩 줄어듦 (안쪽 폭죽이 터질 때 영향)
left -= 1
right -= 1

# 남은 연산 횟수 (N-3)
remain = n - 3

# 남은 횟수만큼 두 더미 중 높은 쪽을 깎아서 최댓값을 최소화
for _ in range(remain):
    if left > right:
        left -= 1
    else:
        right -= 1

# 최종 남은 두 더미 중 최댓값 출력
print(max(left, right))
