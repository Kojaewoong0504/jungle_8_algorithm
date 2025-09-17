import sys
input = sys.stdin.readline
MOD = 1_000_000_000

n = int(input().strip())

if n == 0:
    print(0)
    print(0)
    exit()

m = abs(n)
a, b = 0, 1
for _ in range(m):
    a, b = b % MOD, (a + b) % MOD
if n > 0:
    sign = 1
else:
    if m % 2 == 1:
        sign = 1
    else:                    
        sign = -1

print(sign)
print(a % MOD)

