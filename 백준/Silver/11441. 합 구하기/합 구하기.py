n = int(input())
arr = list(map(int, input().split()))
m = int(input())
prefix = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + arr[i - 1]

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix[j]- prefix[i-1])