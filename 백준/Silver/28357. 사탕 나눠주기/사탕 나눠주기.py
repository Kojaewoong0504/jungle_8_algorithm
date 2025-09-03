import sys
input = sys.stdin.readline

n, k = map(int, input().split())
scores = list(map(int, input().split()))
scores.sort()

left = 0
right = max(scores)
ans = right

while left <= right:
    mid = (left + right) // 2
    candy = 0
    for score in scores:
        if score > mid:
            candy += score - mid

    if candy > k:
        left = mid + 1
    else:
        ans = mid
        right = mid - 1

print(ans)