T = int(input())

N = []
for _ in range(T):
    N.append(list(map(int, input().split())))

for i in N:
    i.sort()
    print(i[-3])