t = int(input())
idx = 1
out = []

for _ in range(t):
    n = int(input())
    idx += 1
    prices = list(map(int, input().split()))
    idx += n

    max_so_far = 0
    profit = 0
    for p in reversed(prices):
        if p < max_so_far:
            profit += max_so_far - p
        else:
            max_so_far = p
    out.append(str(profit))

print("\n".join(out))