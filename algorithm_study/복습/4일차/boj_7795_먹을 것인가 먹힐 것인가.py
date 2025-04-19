from bisect import bisect_left

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()

    cnt = 0
    for i in range(n):
        left = bisect_left(b, a[i])
        cnt += left
    print(cnt)