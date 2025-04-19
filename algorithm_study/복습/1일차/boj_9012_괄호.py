n = int(input())

datas = []

for _ in range(n):
    datas.append(input())


for i in range(n):
    sum = 0
    for j in range(len(datas[i])):
        if datas[i][j] == '(':
            sum += 1
        elif datas[i][j] == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print("YES")