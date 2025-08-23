import sys
import math

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B, X = map(int, input().split())
    g = math.gcd(A, B)
    print(X // g)