n, k = map(int, input().split())

cats = list(map(int, input().split()))
cats.sort()

l, r = 0, n-1
pairs = 0

while l < r:
    if cats[l] + cats[r] <=k:
        pairs += 1
        l += 1
        r -= 1
    else:
        r -= 1

print(pairs)