from bisect import bisect_left,bisect_right

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
arr1.sort()

result = [0] * (m)

for i in range(m):

    left = bisect_left(arr1, arr2[i])
    right = bisect_right(arr1, arr2[i])

    if left != right:
        result[i] = 1

print(*result)