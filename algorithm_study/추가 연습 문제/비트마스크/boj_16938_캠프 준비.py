n, l, r, x = map(int, input().split())
difficulty = list(map(int, input().split()))

count = 0
for i in range(1, 1 << n):
    selected = []
    for j in range(n):
        if i & (1 << j):
            selected.append(difficulty[j])
    if len(selected) < 2:
        continue

    total = sum(selected)
    diff = max(selected) - min(selected)

    if l <= total <= r and diff >= x:
        count += 1

print(count)
