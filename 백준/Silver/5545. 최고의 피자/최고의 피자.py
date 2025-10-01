n = int(input())
a, b = map(int, input().split())
c = int(input())
d = list(int(input()) for _ in range(n))

d.sort(reverse=True)

best_power = c // a
cal = c
price = a

for data in d:
    cal += data
    price += b
    best_power = max(best_power, cal // price)

print(best_power)