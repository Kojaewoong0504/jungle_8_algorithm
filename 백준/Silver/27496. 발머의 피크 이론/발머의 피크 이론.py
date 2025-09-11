import sys
input = sys.stdin.readline

n, l = map(int, input().split())
alc = list(map(int, input().split()))

s = 0
ans = 0
for i in range(n):
    s += alc[i]
    if i >= l:
        s -= alc[i - l]
    if 129 <= s <= 138:
        ans += 1

print(ans)