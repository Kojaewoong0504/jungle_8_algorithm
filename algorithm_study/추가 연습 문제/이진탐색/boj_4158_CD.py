import sys


def find_cd(target, arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False


input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    p1 = [int(input()) for _ in range(n)]
    p2 = [int(input()) for _ in range(m)]

    cnt = sum(1 for cd in p1 if find_cd(cd, p2))

    print(cnt)
