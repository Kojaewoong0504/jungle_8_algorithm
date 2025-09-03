p, n = map(int, input().split())
items = list(map(int, input().split()))
items.sort()

count = 0
total = p
for item in items:
    if total < 200:
        count += 1
        total += item
    else:
        break

print(count)