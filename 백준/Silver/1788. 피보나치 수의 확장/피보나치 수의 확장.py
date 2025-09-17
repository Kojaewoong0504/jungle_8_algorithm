import sys
sys.setrecursionlimit(1 << 25)

MOD = 1_000_000_000

def fib_pair(n: int):
    if n == 0:
        return (0, 1)
    a, b = fib_pair(n >> 1)      # a=F(k), b=F(k+1) where k = n//2
    c = (a * ((2*b - a) % MOD)) % MOD         # F(2k)
    d = (a*a + b*b) % MOD                     # F(2k+1)
    if n & 1:
        return (d, (c + d) % MOD)             # (F(2k+1), F(2k+2))
    else:
        return (c, d)                         # (F(2k), F(2k+1))


n = int(sys.stdin.readline().strip())
if n == 0:
    print(0)
    print(0)
    exit()

m = abs(n)
Fm = fib_pair(m)[0] % MOD

if n > 0:
    sign = 1
else:
    sign = 1 if (m % 2 == 1) else -1

print(sign)
print(Fm)
