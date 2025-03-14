n = int(input())

arr = [True] * (n + 1)
arr[0] = False

for i in range(1, n + 1):
    if i >= 100:
        h = i // 100
        t = (i % 100) // 10
        o = (i % 100) % 10
        if h - t != t - o:
            arr[i] = False
print(arr.count(True))
