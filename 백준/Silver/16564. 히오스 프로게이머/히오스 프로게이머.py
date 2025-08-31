import sys
input = sys.stdin.readline

n, k = map(int, input().split())
members = [int(input()) for _ in range(n)]
members.sort()


max_team_level = 0

left = min(members); right = min(members) + k
ans = left

while left <= right:
    mid = (left + right) // 2

    need = 0
    for x in members:
        if x < mid:
            need += mid - x
        if need > k:
            break

    if need <= k:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)