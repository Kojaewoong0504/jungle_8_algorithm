import sys
input = sys.stdin.readline

n, k = map(int, input().split())
S = list(map(int, input().split()))

l = 0
odds = 0
ans = 0

for r in range(n):
    if S[r] & 1:
        odds += 1

    while odds > k:
        if S[l] & 1:
            odds -= 1
        l += 1

    ans = max(ans, (r - l + 1) - odds)

print(ans)
