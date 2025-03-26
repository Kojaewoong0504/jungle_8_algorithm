x, y = map(int, input().split())

start_rate = (y * 100) // x

if x == y:
    print(-1)
elif start_rate >= 99:
    if ((y + 10**9) * 100) // (x + 10**9) <= start_rate:
        print(-1)
else:
    start, end = 1, 10 ** 9
    while start <= end:
        mid = (start + end) // 2
        new_z = ((y + mid) * 100) // (x + mid)
        if new_z > start_rate:
            end = mid - 1
        else:
            start = mid + 1
    print(start)