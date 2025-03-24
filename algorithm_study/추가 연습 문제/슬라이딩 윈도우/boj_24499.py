n, k = map(int, input().split())
pies = list(map(int, input().split()))


value = sum(pies[:k])
max_value = value
for i in range(k, n+k):
    if i >= n:
        i = i % n
    value += pies[i]
    value -= pies[i-k]
    max_value = max(max_value, value)
print(max_value)