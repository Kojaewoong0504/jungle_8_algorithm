import sys
input = sys.stdin.readline
n, r, c = map(int, input().split())


# def recursion(n, r, c):
#     if n == 1:
#         return 2 * r + c
#
#     half_n = 2 ** (n-1)
#     if r < half_n and c < half_n: #1사분면
#         return 2**(2*(n-1))*0 + recursion(n-1, r, c)
#     elif r < half_n and c>= half_n: #2사분면
#         return 2**(2*(n-1))*1 + recursion(n-1, r-half_n, c)
#     elif r >= half_n and c < half_n: #3사분면
#         return 2**(2*(n-1))*2 + recursion(n-1, r, c-half_n)
#     else: # r >= half_n and c<= half_n: #4사분면
#         return 2**(2*(n-1))*3 + recursion(n-1, r-half_n, c-half_n)
#
#
# print(recursion(n, r, c))


def recursion(n, r, c):
    if n == 0:  # 기저 조건 수정
        return 0

    half_n = 2 ** (n - 1)
    if r < half_n and c < half_n:  # 1사분면
        return recursion(n - 1, r, c)
    elif r < half_n and c >= half_n:  # 2사분면
        return half_n * half_n + recursion(n - 1, r, c - half_n)
    elif r >= half_n and c < half_n:  # 3사분면
        return 2 * half_n * half_n + recursion(n - 1, r - half_n, c)
    else:  # 4사분면
        return 3 * half_n * half_n + recursion(n - 1, r - half_n, c - half_n)

print(recursion(n, r, c))
