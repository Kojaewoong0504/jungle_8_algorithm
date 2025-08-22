import sys
import math

input = sys.stdin.readline

n = int(input().strip())
_ = [list(map(int, input().split())) for _ in range(n)]

code1 = math.comb(2 * n, n)
code2 = n * n

print(code1, code2)