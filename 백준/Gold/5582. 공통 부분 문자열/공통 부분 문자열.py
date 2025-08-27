import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
n, m = len(A), len(B)

prev = [0] * (m + 1)
ans = 0

for i in range(1, n + 1):
    cur = [0] * (m + 1)
    for j in range(1, m + 1):
        if A[i-1] == B[j-1]:
            cur[j] = prev[j-1] + 1
            ans = max(ans, cur[j])
    prev = cur

print(ans)