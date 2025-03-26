
n, k = map(int, input().split())

records = [list(map(int, input().split())) for _ in range(n)]

records.sort(reverse=True, key=lambda x: (x[1], x[2], x[3]))

idx = [records[i][0] for i in range(n)].index(k)

for i in range(k):
    if records[idx][1:] == records[i][1:]:
        print(i+1)
        break