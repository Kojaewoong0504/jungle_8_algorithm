n = int(input())

datas = [list(map(int, input().split())) for _ in range(n)]

datas.sort(key=lambda x: (x[1], x[0]))

for data in datas:
    a, b = data
    print(a, b)
