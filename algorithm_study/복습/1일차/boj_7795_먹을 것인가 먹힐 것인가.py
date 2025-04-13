from bisect import bisect_left


t = int(input())
for _ in range(t):
    count = 0
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    for i in range(n):
        left = bisect_left(B, A[i])
        count += left
    print(count)