import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

prefix = [0] * (n + 1)

for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + arr[i - 1]

result = []

for _ in range(m):
    i, j = map(int, input().split())
    result.append(str(prefix[j] - prefix[i - 1]))

print("\n".join(result))