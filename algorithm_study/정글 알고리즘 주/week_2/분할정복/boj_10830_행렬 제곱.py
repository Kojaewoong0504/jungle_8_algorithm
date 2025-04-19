def matrix_multiply(A, B, mod=1000):
    """
    행렬 A와 B를 곱하고 mod로 나눈 나머지를 반환합니다.
    """
    N = len(A)
    result = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= mod

    return result


def matrix_power(A, B, mod=1000):
    """
    행렬 A의 B제곱을 분할 정복으로 계산하고 mod로 나눈 나머지를 반환합니다.
    """
    N = len(A)

    # B가 0인 경우 단위 행렬 반환
    if B == 0:
        result = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            result[i][i] = 1
        return result

    # B가 1인 경우 A 자체 반환 (mod 적용)
    if B == 1:
        return [[element % mod for element in row] for row in A]

    # 분할 정복: 절반 계산
    half = matrix_power(A, B // 2, mod)

    # 결합: B가 짝수면 half^2, 홀수면 A * half^2
    if B % 2 == 0:
        return matrix_multiply(half, half, mod)
    else:
        return matrix_multiply(A, matrix_multiply(half, half, mod), mod)


# 입력 처리
N, B = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

# 결과 계산 및 출력
result = matrix_power(A, B)
for row in result:
    print(*row)
