

n = int(input())
for i in range(n):
    arr = list(map(int, input().split()))
    t = arr.pop(0)
    avg = sum(arr)/len(arr)
    over = 0
    for j in arr:
        if j > avg:
            over += 1
    print("{:.3f}%".format(over/len(arr)*100))
