n = int(input())

factories = list(map(int, input().split()))

max_value = 0


for i in range(n):
    if i <= n - 3:
        if factories[i+1] > factories[i+2]:
            two = min(factories[i], factories[i+1] - factories[i+2])
            factories[i] -= two
            factories[i+1] -= two
            max_value += two * 5

        three = min(factories[i], factories[i+1], factories[i+2])
        factories[i] -= three
        factories[i+1] -= three
        factories[i+2] -= three
        max_value += three * 7

    if i <= n - 2:
        two = min(factories[i], factories[i+1])
        factories[i] -= two
        factories[i+1] -= two
        max_value += two * 5

    one = factories[i]
    max_value += one * 3
    factories[i] = 0

print(max_value)