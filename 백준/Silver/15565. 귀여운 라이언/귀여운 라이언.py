import sys

input = sys.stdin.readline
n, k = map(int, input().split())
dolls = list(map(int, input().split()))

min_target = float('inf')
count = 0

start = 0
end = 0

if dolls[end] == 1:
    count += 1

while end < n:
    if count == k:
        min_target = min(min_target, end - start + 1)
        if dolls[start] == 1:
            count -= 1
        start += 1
    else:
        end += 1
        if end < n and dolls[end] == 1:
            count += 1

if min_target == float('inf'):
    print(-1)
else:
    print(min_target)
