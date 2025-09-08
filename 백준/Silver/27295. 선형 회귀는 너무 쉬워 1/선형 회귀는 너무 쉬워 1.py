import sys
from math import gcd

input = sys.stdin.readline

n, b = map(int, input().split())
sum_x = 0
sum_y = 0
for _ in range(n):
    x, y = map(int, input().split())
    sum_x += x
    sum_y += y

if sum_x == 0:
    print("EZPZ")
else:
    num = sum_y - n * b     
    den = sum_x             
    if num % den == 0:
        print(num // den)
    else:
        g = gcd(abs(num), abs(den))
        p = num // g
        q = den // g
        if q < 0:
            p, q = -p, -q
        print(f"{p}/{q}")
