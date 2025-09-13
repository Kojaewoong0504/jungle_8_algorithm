import sys
import math

input = sys.stdin.readline

def min_perimeter(n):
    # n의 제곱근 계산
    sqrt_n = math.sqrt(n)

    # 제곱근에 가장 가까운 정수 찾기
    lower = math.floor(sqrt_n)
    upper = math.ceil(sqrt_n)

    # 가능한 직사각형 후보들
    candidates = []

    # lower × lower부터 upper × upper까지 확인
    for width in range(lower, upper + 1):
        for height in range(lower, upper + 1):
            if width * height >= n:  # n개의 정사각형을 모두 포함할 수 있는지
                candidates.append((width, height))

    # 둘레가 최소인 직사각형 찾기
    min_p = float('inf')
    for width, height in candidates:
        perimeter = 2 * (width + height)
        min_p = min(min_p, perimeter)

    return min_p


# 테스트 케이스 처리
t = int(input())
for _ in range(t):
    n = int(input())
    print(min_perimeter(n))
