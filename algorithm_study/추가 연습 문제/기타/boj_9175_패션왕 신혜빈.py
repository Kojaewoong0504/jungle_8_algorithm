t = int(input())


for _ in range(t):
    n = int(input())
    wear = {}

    for i in range(n):
        name, type = map(str, input().split())
        if type not in wear.keys():
            wear[type] = [name]
        else:
            wear[type].append(name)

    count = 1
    for w in wear:
        count *= (len(wear[w]) + 1)
    print(count -1)