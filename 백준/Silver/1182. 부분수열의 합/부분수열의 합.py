from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
for r in range(1, n + 1):
    for comb in combinations(arr, r):
        if sum(comb) == s:
            count += 1

print(count)
