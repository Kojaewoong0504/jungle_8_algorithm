n, k = map(int, input().split())

value = []

for _ in range(n):
    value.append(int(input()))

value.sort(reverse=True)

count = 0

for i in value:
    if k == 0:
        break
    data = k // i
    if data > 0:
        count += data
        k = k % i

print(count)