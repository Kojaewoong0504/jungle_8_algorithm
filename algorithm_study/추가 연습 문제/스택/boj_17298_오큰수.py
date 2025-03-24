import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

stack = [a[-1]]
result = [-1] * n
for i in range(n-2, -1,-1):
    while stack:
        if stack[-1] > a[i]:
            result[i] = stack[-1]
            break
        else:
            stack.pop()
    stack.append(a[i])

print(*result)