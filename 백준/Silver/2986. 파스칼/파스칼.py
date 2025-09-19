import sys
input = sys.stdin.readline

def smallest_divisor(n: int):
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n  # 소수면 자기 자신

N = int(input().strip())
if N == 1:
    print(0)
    exit()
p = smallest_divisor(N)
print(N - (N // p))

