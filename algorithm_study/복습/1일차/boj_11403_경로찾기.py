n = int(input())

input_data = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if input_data[i][k] and input_data[k][j]:
                input_data[i][j] = 1

for i in range(n):
    for j in range(n):
        print(input_data[i][j], end=" ")
    print("")