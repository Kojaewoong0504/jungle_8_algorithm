import sys
n, k = map(int, sys.stdin.readline().split())
dp=[[1]*(n+1) for _ in range(n+1)]
for i in range(2, n+1):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
print(dp[n][k]%1000000007)


# 수학굥식
import sys


def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


def mod_inverse(n, p):
    return power(n, p - 2, p)


def binomial_coefficient(n, k, p):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

    # 팩토리얼 계산
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % p

    # C(n,k) = n! / (k! * (n-k)!)
    return (fact[n] * mod_inverse(fact[k], p) % p * mod_inverse(fact[n - k], p) % p)


n, k = map(int, sys.stdin.readline().split())
MOD = 1000000007
print(binomial_coefficient(n, k, MOD))
