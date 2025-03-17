import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort()
cal = 0
for i in range(len(a)):
    cal += a[i] * b[i]
print(cal)